
note = int(input("Entrez votre note"" "))

if note >= 18:
    print (f"votre note est Excellente")
elif 14<=note<18:
    print (f"votre note est Très bien")
elif 10<=note<14:
    print (f"votre note est Assez bien")
elif 5<=note<10:
    print (f"votre note est Insuffisant")
else :
    print (f"votre note est Catastrophique")