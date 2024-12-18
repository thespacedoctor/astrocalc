fd \\.py  --exec perl -0777 -pi -e 's/:Author:\s*\n\s*/Author\n: /mgs'
fd \\.py  --exec perl -0777 -pi -e 's/:Date Created:\s*\n\s*/Date Created\n: /mgs'
fd \\.py  --exec perl -0777 -pi -e 's/```eval_rst\s*.. todo::\s*?\n*(.*?)\n*(\s*)```/:::{todo}\n$1\n$2:::/mgs'
fd \\.py  --exec perl -0777 -pi -e 's/---\s*:::{todo/:::{todo/mgs'
# fd soxs_mbi.*\\.py  --exec perl -0777 -pi -e 's/( *)\*\*Return:\*\*\s*?\n((\h*(\- .*?\n))+)/$1\*\*Return:\*\*\n\n$1$2/mgs'


count=10
for i in $(seq $count); do
    fd \\.py  --exec perl -0777 -pi -e 's/(?<BLOCK>^(?<INDENT> *)\*\*(Return|Key Arguments):?\*\*\s*?((\g{INDENT}\- [^\n]*?\n)*?))\g{INDENT} +(?<BULLET>\-.*?$\n)/$+{BLOCK}$+{INDENT}$+{BULLET}/gsm'
done
fd \\.py  --exec perl -0777 -pi -e 's/\*\*(Return|Key Arguments):?\*\* *\n( *)-/*\*$1:\*\*\n\n$2-/gsm'


fd \\.md   --exec perl -0777 -pi -e 's/```eval_rst\n\.\. (?<NAME>\S*)::\n(?<CONTENT>.*?)```/:::\{$+{NAME}\}\n$+{CONTENT}:::/gsm'
count=50
for i in $(seq $count); do
    fd \\.md   --exec perl -0777 -pi -e 's/(?<BLOCK>^(?<INDENT> *):::\{\S*\}\s*?\n((\g{INDENT}\S[^\n]*?\n+)*?))\g{INDENT} +(?<BULLET>\S[^\n]*?\n)/$+{BLOCK}$+{INDENT}$+{BULLET}/gsm'
done

fd \\.md   --exec perl -0777 -pi -e 's/\((..\/)?_api\/(?<THIS>\S*?)\.html\)/(#$+{THIS})/gsm'

fd \\.md   --exec perl -0777 -pi -e 's/(\..\/)?_api\/\S*?\.html#/#/gsm'

fd \\.py   --exec perl -0777 -pi -e 's/`see tutorial here <http:\/\/fundamentals.readthedocs.io\/en\/latest\/#tutorial>`_/see tutorial here https:\/\/fundamentals.readthedocs.io\/en\/master\/initialisation.html/gsm'

# fd \\.md docs/source/recipes/  --exec perl -0777 -pi -e 's/### (Output|Input|Method|QC Metrics|Parameters|Recipe API)/## $1/gsm'

fd \\.md  --exec perl -0777 -pi -e 's/^\{\{(\S*)\}\}/:::\{include\} $1\n:::/gsm'


fd \\.md   --exec perl -0777 -pi -e 's/```mermaid\n(?<CONTENT>.*?)```/:::{mermaid}\n$+{CONTENT}:::/gsm'


fd \\.md   --exec perl -0777 -pi -e 's/```eval_rst\n\.\. autoclass:: soxspipe\.(recipes|commonutils)\.(\S*).*?```/:::\{autodoc2-object\} soxspipe.$1.$2.$2\n:::/gsm'


fd \\.md   --exec perl -0777 -pi -e 's/```eval_rst\n\.\. automethod:: soxspipe\.(recipes|commonutils)\.(\S*).*?```/:::\{autodoc2-object\} soxspipe.$1.$2\n:::/gsm'



