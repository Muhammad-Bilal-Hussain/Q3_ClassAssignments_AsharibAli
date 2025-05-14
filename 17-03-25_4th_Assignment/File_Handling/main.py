# File Handling Kya Hoti Hai?
# File handling ka matlab hai file ko read (parhna) ya write (likhna) karna — yani jab hum data ko kisi file me save karte hain ya wahan se nikaalte hain.

# Python me ye kaam built-in functions ke zariye hota hai. Iska fayda ye hai ke hum data ko permanent (save) rakh sakte hain, program band hone ke baad bhi.

# 🔹 File Ko Open Karna
# Python me file open karne ke liye open() function use hota hai.
# Iske andar do cheezen deni hoti hain:

# python
# Copy
# Edit
# open("filename", "mode")
# filename: jiska naam tumhari file ka hai (jaise "data.txt")

# mode: file ko kis tareeke se open karna hai (read, write, etc.)

# 🔸 File Opening Modes (Tareeqe):
# Mode	Kya karta hai?
# r	Read mode: file ko parhta hai. (Default hai)
# w	Write mode: file ko likhne ke liye open karta hai. Agar file exist karti hai to overwrite kar dega. Agar nahi hai to create kar deta hai.
# a	Append mode: file ke end me naya content add karta hai. Purani cheezen delete nahi hoti. Agar file nahi hai to bana deta hai.
# x	Exclusive Creation: sirf tab file create karega jab wo pehle se na ho. Agar already exist karti hai to error dega.
# b	Binary mode: images, audio, ya binary files ke sath kaam karne ke liye hota hai (use hota hai rb, wb, etc ke sath).
# +	Update mode: read aur write dono ek sath karne ke liye use hota hai (jaise r+, w+).


# 1. File Create & Write (write mode)
file = open("example.txt", "w")
file.write("Hello! Ye pehla line hai file me.")
file.close()

#2. File Read (read mode)
file = open("example.txt", "r")
content = file.read()
print("File ka content:", content)
file.close()

# 3. Append to File (without overwriting)
# file me naye line add karna (purani delete nahi hoti)
file = open("example.txt", "a")
file.write("\nYe second line hai.")
file.close()

# 4. Read Line by Line (loop se)
# har line ko alag alag read karna
file = open("example.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# 5. With Statement (auto close file)
# best practice: file khud ba khud close ho jati hai
with open("example.txt", "r") as file:
    data = file.read()
    print("File content with 'with':", data)
