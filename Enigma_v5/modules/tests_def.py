# only functions to generate tools for ten drums tests encrypts
from collections import Counter
import decimal

from math import log
from random import randint

from Enigma_all.Enigma_v5.modules.test_print import test_print
from Enigma_all.Enigma_v5.modules.tools import save_rotors, load_rotors, encrypt, decrypt, gen_text, check_patterns, \
    create_key, check_all_patterns, create_rotors, key_from_64b_to_dec, load_key, create_random_64b_key, load_file, save_file, save_key


# from Enigma_all.Enigma_v5.modules.__tools_single import generate_from_64b_inter_key

def test_3r_2b (show_all=False, show_first=False, show_short=False, show_calc=False):
    try:
        rotors = load_rotors("./rotors/set_drum_2b_", 3)
    except:
        rotors = {0: 2, 1: 0, 2: 3, 3: 1}, {0: 3, 1: 2, 2: 0, 3: 1}, {0: 3, 1: 0, 2: 1, 3: 2}
        save_rotors(rotors,"./rotors/set_drum_2b_")
    
    key_enc = "17as"
    key_enc = "aegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgs"
    # key_enc = [0, 2, 2, 0, 1, 2]#, 3, 3, 3]

    # key_dec = "17as"
    # key_dec = "aegfsdsg24r34qg"
    key_dec = "aegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsaegfsdsg24r34qsadfasdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfasdfasfsgsdfhdfjgkljshsdfsdfsdfassdfasfsgssdfasfsgsdfhdfjgkljshsdfssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsfsgssfsgsdfhdfjgkljshsdfsdfsdfasfsgsssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgsdfhdfjgkljshsdfgasdfagrshgjgjdfjsdgeshdfjdfgsdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgssdfasfsgsdfhdfjgkljshsdfsdfsdfasfsgs"
    # key_dec = [0, 2, 2, 0, 1, 2]#, 3, 3, 3]
   
    
    # def gen_text(char_max, ran, size_triple, drum_for_gen, *char_size):
    text_before = gen_text(0, False, False, rotors[0], 0, 100)

    text_encrypt = encrypt(rotors, key_enc, text_before) # todo zmień kolejność txt pierwzy rotors i key
    text_decrypt = decrypt(rotors, key_dec, text_encrypt)

    # def test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt,
    #                show_all=True, show_first=False, show_short=False, show_calc=False):
    test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all,  show_first, show_short, show_calc)


def test_5r_8b(show_all=True, show_first=False, show_short=False, show_calc=False):
    try:
        rotors = load_rotors("./rotors/set_drum_8b_", 5)
    except:
        rotors = create_rotors(8, True, 5)
        save_rotors(rotors, "./rotors/set_drum_8b_")
    
    key_enc = "7V9AFEGDJFHasdfdwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwfadsf23JSDF233"
    
    key_dec = "7V9AFEGDJFHasdfdwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwfadsf23JSDF233"
    
    # def gen_text(char_max, ran, size_triple, drum_for_gen, *char_size):
    text_before = gen_text(0, False, False, rotors[0], 0, 100)
    
    text_encrypt = encrypt(rotors, key_enc, text_before)
    text_decrypt = decrypt(rotors, key_dec, text_encrypt)
    
    # def test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt,
    #                show_all=True, show_first=False, show_short=False, show_calc=False):
    test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all, show_first, show_short,
               show_calc)


def test_5r_8b_file_txt_encrypt(show_all=True, show_first=False, show_short=False, show_calc=False):
    
    rotors = {}
    try:
        rotors = load_rotors("./rotors/set_drum_8b_", 5)
    except:
        rotors = create_rotors(8, True, 5)
        save_rotors(rotors, "./rotors/set_drum_8b_")
    
    try:
        key = load_key("./keys/do_txt")
    except:
        key = create_random_64b_key(size_in_bit=1024)
        save_key("./keys/do_txt", key)
    
    text_before = load_file("bajka2.txt")
    
    print(text_before)
    
    text_encrypt = encrypt(rotors, key, text_before)
    print(text_encrypt)
    text_encrypt.append(ord("\n"))
    print(text_encrypt)
    save_file("bajka2.txt.enc", text_encrypt)

def test_5r_8b_file_txt_decrypt(show_all=True, show_first=False, show_short=False, show_calc=False):

    rotors = {}
    try:
        rotors = load_rotors("./rotors/set_drum_8b_", 5)
    except:
        rotors = create_rotors(8, True, 5)
        save_rotors(rotors, "./rotors/set_drum_8b_")

    try:
        key = load_key("./keys/do_txt")
    except:
        key = create_random_64b_key(size_in_bit=1024)
        save_key("./keys/do_txt", key)

    text_encrypt = load_file("bajka2.txt.enc")

    print(text_encrypt)

    text_decrypt = decrypt(rotors, key, text_encrypt[:-1])

    save_file("bajka2.txt.dec", text_decrypt)
    
    
    # text_decrypt = decrypt(rotors, key_dec, text_encrypt)
    
    # def test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt,
    #                show_all=True, show_first=False, show_short=False, show_calc=False):
    # test_print(rotors, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all, show_first, show_short,
    #            show_calc)

