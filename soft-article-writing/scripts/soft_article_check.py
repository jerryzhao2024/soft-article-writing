#!/usr/bin/env python3
"""Basic checks for a soft article draft."""
from pathlib import Path
import argparse, re, sys

AI_PHRASES = [
    '随着', '在当今时代', '众所周知', '让我们来看看', '总而言之', '综上所述',
    '赋能', '闭环', '抓手', '生态化', '你值得', '愿你',
]
ABSOLUTE_PHRASES = [
    '全网第一', '行业第一', '国内第一', '零故障', '零停机', '100%密封', '全适配', '全机型',
]
UNSOURCED_MARKERS = ['据行业数据', '据统计', '业内人士', '专家认为', '研究表明']

def read_text(path):
    p = Path(path)
    if p.suffix.lower() == '.docx':
        try:
            from docx import Document
            return '\n'.join(x.text for x in Document(p).paragraphs)
        except Exception as e:
            raise SystemExit(f'无法读取 DOCX: {e}')
    return p.read_text(encoding='utf-8')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('article')
    args = ap.parse_args()
    text = read_text(args.article)
    paragraphs = [x.strip() for x in text.splitlines() if x.strip()]
    issues = []
    if len(paragraphs) < 5:
        issues.append('段落过少，可能缺少导语、正文或 CTA')
    compact = re.sub(r'\s+', '', text)
    if len(compact) < 350:
        issues.append('正文偏短，可能只有摘要或提纲')
    for phrase in AI_PHRASES:
        if phrase in text:
            issues.append(f'AI/套话候选: {phrase}')
    for phrase in ABSOLUTE_PHRASES:
        if phrase in text:
            issues.append(f'绝对化表达: {phrase}')
    for phrase in UNSOURCED_MARKERS:
        if phrase in text:
            issues.append(f'未注明来源的表述: {phrase}')
    # Repeated paragraphs are the most common template symptom.
    seen = {}
    for i, para in enumerate(paragraphs):
        if len(para) < 30:
            continue
        if para in seen:
            issues.append(f'重复段落: 第 {seen[para]+1} 和第 {i+1} 段')
        else:
            seen[para] = i
    if issues:
        print('\n'.join(f'- {x}' for x in issues))
        sys.exit(1)
    print(f'OK: {args.article} 基础检查通过')

if __name__ == '__main__':
    main()
