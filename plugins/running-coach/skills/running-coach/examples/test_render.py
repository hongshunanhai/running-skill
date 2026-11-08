import json
import subprocess
import sys
import tempfile
from pathlib import Path
from xml.etree import ElementTree

root = Path(__file__).resolve().parents[1]
with tempfile.TemporaryDirectory() as tmp:
    source = Path(tmp) / 'in.json'
    output = Path(tmp) / 'out.svg'
    data = json.loads((root / 'examples/sample.json').read_text())
    data['insight'] = '恢复 < 训练 & 休息'
    source.write_text(json.dumps(data, ensure_ascii=False))
    subprocess.run([sys.executable, str(root / 'scripts/render_report.py'), str(source), str(output)], check=True)
    tree = ElementTree.parse(output)
    text = ''.join(tree.getroot().itertext())
    assert '32.4' in text and '暂无数据' in text and '恢复 < 训练 & 休息' in text
    data['insight'] = '注意恢复' * 30
    source.write_text(json.dumps(data, ensure_ascii=False))
    subprocess.run([sys.executable, str(root / 'scripts/render_report.py'), str(source), str(output)], check=True)
    tree = ElementTree.parse(output)
    spans = tree.findall('.//{http://www.w3.org/2000/svg}tspan')
    assert len(spans) >= 2
    data['daily'][0]['km'] = -1
    source.write_text(json.dumps(data, ensure_ascii=False))
    result = subprocess.run([sys.executable, str(root / 'scripts/render_report.py'), str(source), str(output)], capture_output=True)
    assert result.returncode != 0
print('report tests passed')
