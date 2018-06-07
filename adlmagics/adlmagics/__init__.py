from adlmagics.adlmagics_main import AdlMagics

def load_ipython_extension(ipython):
    ipython.register_magics(AdlMagics)