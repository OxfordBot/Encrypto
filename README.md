## Encrypto ##
Grade 3 Military Encryption Software developed using Python.
### Installation ###
Installing Encrypto is easy. Type the following code shown below in your command prompt.
```bash
git clone https://github.com/OxfordBot/Encrypto.git
```
### How to Use ###
* Open your IDE.
* Import the module by typing the code shown below.
```python
import encrypto
```
* Import the Encrypto class by typing the code shown below.
```python
app = encrypto.Encrypto()
```
* Create an encryption key by typing the code shown below.
```python
key = app.generate_key()
```
* To encrypt a text and show it, type the following code shown below.     
<kbd>Replace the "Encrypto." with the text you want to encrypt<br>and enter the key that you generated in step 4.</kbd>
```python
encrypted_text = app.encrypt("Encrypto.", key)
print(encrypted_text)
```
* To decrypt a text and show it, type the following code shown below.     
<kbd>Replace the "5;/,,2557*C>;B0<?:GKCIIIGLNMKSQYXF" with the text you want to encrypt<br>and enter the key that you generated in step 4.</kbd>
```python
decrypted_text = app.decrypt("5;/,,2557*C>;B0<?:GKCIIIGLNMKSQYXF", key)
print(decrypted_text)
```
* Done! You have successfully completed the steps.<br>There are also some examples you can follow that are shown below.<br>      
    - Encrypting a text.
         ```python
         import encrypto
         app = encrypto.Encrypto()
         key = app.generate_key()
         encrypted_text = app.encrypt("Encrypto.", key)
         print(encrypted_text)
         ```
    - Decrypting a text
       ```python 
       import encrypto
       app = encrypto.Encrypto()
       key = app.generate_key()
       decrypted_text = app.decrypt("5;/,,2557*C>;B0<?:GKCIIIGLNMKSQYXF", key)
       print(key)
       ```
      
