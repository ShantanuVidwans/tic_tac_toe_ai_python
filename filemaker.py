f = open("db","w")
arr =["X","O","0"]
out = ["0","0","0","0","0","0","0","0","0"]
jon = ""
res = ""
for x0 in arr:
    for x1 in arr:
        for x2 in arr:
            for x3 in arr:
                for x4 in arr:
                    for x5 in arr:
                        for x6 in arr:
                            for x7 in arr:
                                for x8 in arr:
                                    out[8] = x8
                                    f.write(jon.join(out))
                                    out1 = out.copy()
                                    count = 0
                                    for x in out1:
                                        if x == "0":
                                            out1[count] = "1"
                                            f.write(',' + jon.join(out1) + '10000')
                                            out1 = out.copy()
                                        count = count + 1
                                    f.write("\n")

                                out[7] = x7
                            out[6] = x6
                        out[5] = x5
                    out[4] = x4
                out[3] = x3
            out[2] = x2
        out[1] = x1
    out[0] = x0





