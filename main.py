import time
def encrypt(txtfilename,key,blocksize):
    start_time = time.time()

    encryptedtext = ""
    cycle= 2*(key-1)

    with open(txtfilename, "r", encoding='utf-8') as txtfile:
        while True:
            block = txtfile.read(blocksize).replace("\n","\t")
            for row in range(key):
                index = key-1
            # first row
                if row == 0:
                    while index < len(block):
                        encryptedtext += block[index]
                        index += cycle


                # last row
                elif row == key-1:
                    index = 0
                    while index < len(block):
                        encryptedtext += block[index]
                        index+=cycle


                # middle row
                else:
                    left_index = row
                    right_index = cycle - row
                    while left_index < len(block):
                        encryptedtext += block[left_index]
                        if right_index < len(block):
                            encryptedtext += block[right_index]
                        left_index += cycle
                        right_index += cycle

            if not block:
                break


    result=encryptedtext
    #print(result)
    end_time = time.time()
    total_time = end_time - start_time
    print("Час виконання шифрування: ", total_time, "секунд")
    with open("encryptednew1.txt", "w", encoding="utf-8") as outputfile:
        outputfile.write(result)

    return result



def decrypt(txtfilename,key,blocksize):
    with open(txtfilename, "r", encoding="utf-8") as encryptedtxtfile:
        result = ''
        cycle = 2 * (key - 1)
        start_time = time.time()
        while True:
            block = encryptedtxtfile.read(blocksize)

            length = len(block)
            finaltext = "@" * len(block)

            cycle_amount = length // cycle
            lengths_of_rail = [0] * key


            # first row
            lengths_of_rail[0] = cycle_amount


            # mid rows
            for i in range(1, key - 1):
                lengths_of_rail[i] = 2 * cycle_amount



            # last row
            lengths_of_rail[key - 1] = cycle_amount
            for i in range(length % cycle):
                if i < key:
                    lengths_of_rail[i] += 1
                else:
                    lengths_of_rail[cycle - i] += 1
            index = key-1




            # first row
            for char in block[:lengths_of_rail[key-1]]:
                finaltext = finaltext[:index] + char + finaltext[index + 1:]
                index += cycle
            railoffset = 0
            railoffset += lengths_of_rail[key-1]
            #print(finaltext)

            # mid rows
            for row in range(1, key - 1):
                left_index = row
                right_index = cycle - row
                from_the_left = True
                for char in block[railoffset:railoffset + lengths_of_rail[row]]:
                    if from_the_left:
                        finaltext = finaltext[:left_index] + char + finaltext[left_index + 1:]
                        left_index += cycle
                        from_the_left = not from_the_left
                    else:
                        finaltext = finaltext[:right_index] + char + finaltext[right_index + 1:]
                        right_index += cycle
                        from_the_left = not from_the_left
                railoffset += lengths_of_rail[row]
                #print(finaltext)

            # last row
            index = 0
            for char in block[railoffset:]:
                finaltext = finaltext[:index] + char + finaltext[index + 1:]
                index += cycle
            result += finaltext.replace("\t", "\n")
            with open("decryptednew1.txt", "w", encoding="utf-8") as outputfile:
                outputfile.write(result)
            #result+=finaltext.replace("\t","\n")
            if not block:
                break

        #del result
        end_time = time.time()
        total_time = end_time - start_time

        print('Час дешифрування', total_time)





txtfile = "input.txt"
key = 3
blocksize = 20

encrypted_result = encrypt(txtfile, key, blocksize)
decrypted_result = decrypt("encryptednew1.txt", key, blocksize)