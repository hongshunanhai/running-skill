#!/usr/bin/env python3
"""Render a compact running report from verified, explicitly supplied data."""
import html
import json
import math
import sys
import unicodedata
from pathlib import Path


def esc(value):
    return html.escape(str(value), quote=True)


def number(value):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
        raise ValueError('numbers must be finite and non-negative, or null')
    return value


def wrap_text(value, limit=62, max_lines=2):
    lines, line, width = [], '', 0
    for char in str(value).replace('\n', ' '):
        size = 2 if unicodedata.east_asian_width(char) in ('W', 'F') else 1
        if width + size > limit:
            lines.append(line)
            line, width = '', 0
        line += char
        width += size
    if line:
        lines.append(line)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1][:-1] + '…'
    return lines or ['']


def render(data):
    daily = data.get('daily', [])
    if not isinstance(daily, list) or len(daily) > 12:
        raise ValueError('daily must be a list of at most 12 entries')
    vals = [number(item.get('km')) for item in daily]
    metrics = [number(data.get(key)) for key in ('distance_km', 'runs', 'minutes')]
    label = lambda value: '—' if value is None else f'{value:g}'
    maximum = max([v for v in vals if v is not None] or [1]) or 1
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350">',
           '<rect width="1080" height="1350" fill="#0c1d2b"/>',
           '<style>text{font-family:Arial,"PingFang SC","Microsoft YaHei",sans-serif;fill:#f2f3e9}.muted{fill:#a8bfbd}.small{font-size:24px}.label{font-size:22px}.big{font-size:58px;font-weight:700}</style>',
           '<text x="70" y="85" fill="#65e5c0" font-size="24" letter-spacing="4">RUNNING / REPORT</text>',
           f'<text x="70" y="158" font-size="48" font-weight="700">{esc(data.get("title", "跑步报告"))}</text>',
           f'<text x="70" y="207" class="muted small">{esc(data.get("period", ""))}</text>',
           '<rect x="60" y="250" width="960" height="220" rx="28" fill="#173342"/>']
    for x, value, title, unit in zip((100, 415, 730), metrics, ('总距离', '跑步次数', '训练时长'), ('km', '次', '分钟')):
        out.extend([f'<text x="{x}" y="315" class="muted label">{title}</text>',
                    f'<text x="{x}" y="390" class="big">{label(value)}</text>',
                    f'<text x="{x}" y="430" class="muted label">{unit}</text>'])
    out.extend(['<text x="70" y="560" font-size="32" font-weight="700">跑量分布</text>',
                '<text x="70" y="600" class="muted small">公里 / 每个时间段</text>',
                '<line x1="90" y1="980" x2="990" y2="980" stroke="#627d7f" stroke-width="2"/>'])
    if not daily:
        out.append('<text x="450" y="800" class="muted small">暂无数据</text>')
    for i, (item, value) in enumerate(zip(daily, vals)):
        width = 880 / max(len(daily), 1)
        x = 100 + i * width
        bar = min(60, width * .55)
        height = 290 * value / maximum if value is not None else 0
        if value is not None:
            out.append(f'<rect x="{x:.1f}" y="{980-height:.1f}" width="{bar:.1f}" height="{height:.1f}" rx="8" fill="#65e5c0"/>')
        display = '暂无数据' if value is None else f'{value:g}'
        out.append(f'<text x="{x:.1f}" y="{min(950, 960-height):.1f}" class="muted" font-size="18">{display}</text>')
        out.append(f'<text x="{x:.1f}" y="1020" class="muted" font-size="18">{esc(item.get("label", ""))}</text>')
    lines = wrap_text(data.get('insight', '暂无建议'))
    out.extend(['<rect x="60" y="1080" width="960" height="150" rx="24" fill="#173342"/>',
                '<text x="90" y="1130" fill="#65e5c0" font-size="22">训练提示</text>',
                '<text x="90" y="1170" font-size="24">' + ''.join(
                    f'<tspan x="90" dy="{0 if i == 0 else 32}">{esc(line)}</tspan>' for i, line in enumerate(lines)) + '</text>',
                f'<text x="70" y="1290" class="muted" font-size="18">{esc(data.get("source", "来源未提供"))}</text></svg>'])
    return '\n'.join(out)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('usage: render_report.py INPUT.json OUTPUT.svg')
    Path(sys.argv[2]).write_text(render(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))), encoding='utf-8')
