import os

txt_path = "./cmp_top.txt"
if os.path.exists(txt_path) is False:
    print(f"Warning: not found '{txt_path}', skip this annotation file.")


with open(txt_path) as fid:
                txt_str = fid.readlines()
                #txt_str = fid.read()

print(type(txt_str))

txt_path = "./cmp_top_write.txt"

items = {}
for item in txt_str:
#    print(item)
    print("done",end="\n")
    item = item.strip()   
    item = item.split()
#    items.ext
    print(len(item))
    if (len(item) > 7):
        if("0402" in item[2]):
            #print("item2 shape is:\n",item[2].shape)
            with open(txt_path,mode='a') as fid:
                fid.writelines(item[0])
                fid.writelines("\t")
                fid.writelines(item[2])
                fid.writelines("\t")
                fid.writelines(item[3])
                fid.writelines("\t")
                fid.writelines(item[4])
                fid.writelines("\t")
                fid.writelines(item[7])
                fid.writelines("\n")
    i=0
    for subitem in item:
        i=i+1
        print(i,end=" ")
        print(subitem,end=" ")
    print("\n")
    


            #fid.writelines("kasgfsdjgkl;sdjkl\tksajfksdjf\nkdswjfksj fkjskend")
            


#def del_2\t