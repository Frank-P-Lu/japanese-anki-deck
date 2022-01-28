from dataclasses import dataclass
from typing import List


@dataclass
class Kanji:
    kanji: str
    reading: str
    english: List[str]


kanjis = [
    Kanji('折る', 'おる', ['to break','to fracture','to break off','to snap off','to pick (e.g. flowers)']),
    Kanji('合わせる', 'あわせる', ['to match (rhythm, speed, etc.)']),
    Kanji('枚', 'まい', ['counter for flat objects (e.g. sheets of paper)']),
    Kanji('軽い', 'かるい', ['light (i.e. not heavy)','feeling light (i.e. offering little resistance, moving easily)']),
    Kanji('治る', 'なおる', ['to get better','to get well','to recover (from an illness)','to be cured','to be restored','to heal']),
    Kanji('線', 'せん', ['line','stripe','stria']),
    Kanji('ひっくり返す', 'ひっくりかえす', ['to turn over','to turn upside down','to turn up','to turn inside out','to turn out']),
    Kanji('閉じる', 'とじる', ['to close (e.g. book, eyes, meeting, etc.)','to shut']),
    Kanji('生かす', 'いかす', ['to make (the best) use of','to put to good use','to leverage (skills, attributes, experience, etc.)','to capitalise on (experience, etc.)']),
    Kanji('技術', 'ぎじゅつ', ['technology','engineering']),
    Kanji('先', 'さき', ['point','tip','end','nozzle']),
    Kanji('通す', 'とおす', ['to stick through','to force through']),
    Kanji('火事', 'かじ', ['fire','conflagration']),
    Kanji('に関して', 'にかんして', ['related to','in relation to','as far as ... is concerned']),
    Kanji('個', 'こ', ['counter for articles']),
    Kanji('側', 'がわ', ["side (of something, or taking someone's side)","part"]),
    Kanji('角', 'かく', ['angle']),
    Kanji('特徴', 'とくちょう', ['feature','trait','characteristic','peculiarity','distinction']),
    Kanji('植物', 'しょくぶつ', ['plant','vegetation']),
    Kanji('光', 'ひかり', ['light']),
    Kanji('手作り', 'てづくり', ['handmade','homegrown','hand-crafted','homemade']),
    Kanji('和紙', 'わし', ['washi','Japanese paper']),
    Kanji('三角', 'さんかく', ['triangle','triangular shape']),
    Kanji('分かれる', 'わかれる', ['to branch','to fork','to diverge']),
    Kanji('第一', 'だいいち', ['first','foremost','number one']),
    Kanji('入院', 'にゅういん', ['hospitalization','hospitalisation']),
    Kanji('仲良くする', 'なかよく', ['on good terms (with)','on friendly terms (with)','(getting along) well','in harmony','happily','peacefully']),
    Kanji('頭', 'あたま', ['head']),
]

with open('c12_kanji.csv', 'w') as file:
    kanji: Kanji
    file.write('Kanji; Reading; English\n')
    for kanji in kanjis:
        line = ";".join([kanji.kanji, kanji.reading, ", ".join(kanji.english)]) + '\n'
        file.write(line)


