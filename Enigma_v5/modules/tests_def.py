# only functions to generate tools for ten drums tests encrypts
from Enigma_all.Enigma_v5.modules.test_print import test_print
from Enigma_all.Enigma_v5.modules.tools import save_drums, load_drums, encrypt, decrypt, gen_text


def test_3d_2b ():
    drums = load_drums("./drums/set_drum_2b_", 3)
    drums = {0: 2, 1: 0, 2: 3, 3: 1}, {0: 3, 1: 2, 2: 0, 3: 1}, {0: 3, 1: 0, 2: 1, 3: 2}
    # drum1 = {0: 2, 1: 0, 2: 3, 3: 1}
    # drum2 = {0: 3, 1: 2, 2: 0, 3: 1}
    # drum3 = {0: 3, 1: 0, 2: 1, 3: 2}
    key_enc = [0, 2, 2, 0, 1, 2, 3, 3, 3]#, 1, 1, 3]#, 3, 3]
    key_dec = [0, 2, 2, 0, 1, 2, 3, 3, 3]#, 1, 1, 3]#, 3, 3]
    text_before = [0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3]
    text_before = gen_text(0, False, False, drums[0], 3, 1000)
    # print(text_before)
    text_encrypt = encrypt(drums, key_enc, text_before)
    print("Enc ready")
    text_decrypt = decrypt(drums, key_dec, text_encrypt)
    print("Dec ready")
    #def test_print(drums, key_enc, key_dec, text_before, text_encrypt, text_decrypt, show_all=True):
    test_print(drums, key_enc, key_dec, text_before, text_encrypt, text_decrypt, False)
    
    print("-----")
    # todo to jest 3 pod rząd !!!!
    text_decrypt_first = [0, 0, 1, 2, 3, 0, 0, 1, 2, 3, 0, 0, 1, 2, 3]
    # text_decrypt_first = gen_text(0, True, False, drums[0], 3, 1000) + text_decrypt_first
    text_decrypt_2 = text_decrypt_first[:]
    list_of_patterns = []
    a = 2
    nr_del = 0
    while True:
        for i in range(0, len(text_decrypt_2)):
            if (a + i) * 3 > len(text_decrypt_2):
                break
            if text_decrypt_2[0: a + i] == text_decrypt_2[a + i: (a + i) * 2] == text_decrypt_2[(a + i) * 2: (a + i) * 3]:
                list_of_patterns.append([len(text_decrypt_2[0: a + i]), nr_del, nr_del + (a + i) * 3 - 1])
        if len(text_decrypt_2) >= 1:
            text_decrypt_2.pop(0)
        else:
            break
        nr_del += 1
    print(list_of_patterns)
    # print(text_decrypt_2[list_of_patterns[-1][1]:list_of_patterns[-1][2] + 10 ])
    
    
    # todo tutaj będzie jakie kolwiek
    text_decrypt_3 = text_decrypt_first[:]
    min = 3
    list_of_patterns_2 = []
    nr_del_2 = 0
    while True:
        for i in range(0, len(text_decrypt_3)):
            # if 2*min + i > len(text_decrypt_3):
            #     break
            if text_decrypt_3[0: min] == text_decrypt_3[min + i: 2*min + i]:
                list_of_patterns_2.append([min, nr_del_2, min + nr_del_2 -1])
        if len(text_decrypt_3) >= 1:
            text_decrypt_3.pop(0)
        else:
            break
        if min < len(text_decrypt_3):
            min += 1
        else:
            text_decrypt_3 = text_decrypt_first[:]
            min = 3
            nr_del_2 += 1
        if nr_del_2 > len(text_decrypt_3):
            break
    print(list_of_patterns_2)
    
#
# drums_bit = 8
# debug = True # todo przenieś to głównego ???
# random_drums = True
# random_text_before = True
# dir_name = ""
#
# size_drums = 2 ** drums_bit
#
# # drums generate and save
# create_and_save_dicts(create_drums(size_drums, random_drums), ("../drums/drum2b_"))
#
# # drums load
# drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
# drum2b_8, drum2b_9, drum2b_10 = load_drums("../drums/drum2b_")
#
# # drums check
# check_rand_dicts(load_drums("../drums/drum2b_"), debug) #todo FORMATOWANIE PASS!!!
#
# # (Char_max, ran, size_double, drum_for_gen, char, size)
# # todo napisz to po angielsku
# # text_before = gen_text(False, False, False, drum2b_1)
#
# # text_before = "dupa jaś"
# # from Enigma_all.Enigma_4.modules.__tools_single import __save_drum, __load_drum
# #
# # __save_drum(text_before)
#
#
# #
# #
# # y = load_10_dicts("../drums/drum2b_")
# # print(y)
# # drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7, \
# # drum2b_8, drum2b_9, drum2b_10 = y
#
# # print("-------")
# # print(drum2b_1)
# # print("--------------------------------------------------------------------")
# # print("Text before: \t", str(text_before[0:11]).replace("]", ", + ... ]\t"),
# #       format(decimal.Decimal(len(text_before)), '.2E')) if len(str(text_before)) >= 11 else \
# #     print("Text before: \t", text_encrypt)
# # print("Text encrypt:\t", str(text_encrypt[0:15]).replace("]", ","), "...]")
# # print("Text decrypt:\t", str(text_decrypt[0:15]).replace("]", ","), "...]")
# # print("--------------------------------------------------------------------")
#
#
#
#
#
#
# # def test_10d_2b_1d_1c_tk_rand
# # def test_10d_2b_1d_1c_tk_min
# # def test_10d_2b_1d_1c_tk_max
#
#
#
#
# # def test_10d_4b_4d_300c_tk_():
#
#
# # drum2b_1, drum2b_2, drum2b_3, drum2b_4, drum2b_5, drum2b_6, drum2b_7,\
# # drum2b_8, drum2b_9, drum2b_10 = create_10_dicts(size_drums, True)