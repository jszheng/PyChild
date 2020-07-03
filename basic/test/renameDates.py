import shutil, os, re

Datesearch = re.compile(r""""^(.*?)
((0|1)?\d)-
((0|1|2|3)?\d)-
((19|20)\d\d)
(.*?)$
""", re.VERBOSE)
for AmerFile in os.listdir():
    mo = Datesearch.search(AmerFile)
    if mo == None:
        continue

    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4)
    yearpart = mo.group(6)
    afterpart = mo.group(8)

    Datesearch = re.compile(r"""^(1)
    (2 (3) )-
    (4 (5) )-
    (6 (7) )-
    (8)$
    """, re.VERBOSE)

    euroFilename = beforepart + daypart + '-' + monthpart + '-' + yearpart + afterpart

    absWorkingDir = os.path.abspath('.')
    AmerFile = os.path.join(absWorkingDir, AmerFile)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Rename "%s" to "%s" ...' % (AmerFile, euroFilename))
    # shutil.move(Amerfile, eurofilename)
