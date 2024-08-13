

# Install library
--------------------------------------------------
- RUN "pip3 install requirement.txt"

# Initialize
--------------------------------------------------
- RUN "./gencode --gen-type common"        to generate "common"    code at "./output/common"
- RUN "./gencode --gen-type impl"          to generate "implement" code at "./output/impl"
- RUN "cp -r output/common/* vht/common/." to use generated code

# Debug
- RUN "diff -r output/impl vht/impl"        to show custom code

## BUILD
--------------------------------------------------
- RUN "pyinstaller -F netconf_cli_agent.py" to build executable file at dist/netconf_cli_agent

## INSTALL
- DESTDIR=$PACKAGE make install