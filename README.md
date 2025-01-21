# ![alphascript](https://github.com/user-attachments/assets/a2f8dd94-a781-4716-80a6-8b673f28f073) DAV-Alpha-Shader-Replacer-Tool

Automatically convert shaders within .bin MeshVariationDB files to 2SidedAlpha.

Values can be customized.

## How to Use

Place the executable and guids.txt in a folder. Create a directory called "binary files" in the same folder.

![01](https://github.com/user-attachments/assets/1a3c5fea-c4a7-4e81-8a58-e66805d08db1)

Place all the files you want to convert in the "binary files" folder.

![02](https://github.com/user-attachments/assets/27af6272-5bca-4146-91b0-db0c6ab3bbd1)

Double click the executable to run it. If you placed everything correctly, the modified bin files will appear in the folder where the executable is located.

They will match the file names of the original file with "_modified" appended at the end. These files are ready to be imported back into the Frosty Editor!

![03](https://github.com/user-attachments/assets/9799cb62-611b-4793-b14a-5d750bf133b3)

## Customize guids.txt

You can use the included guids.txt file, which includes all the values provided by [Joell560](https://next.nexusmods.com/profile/Joell560?gameId=6945).

If you want to customize these values, add the hex value you want to replace on a new line, followed on the next line by the hex value you want to replace it with. Values can be a continuous string or separated into bytes with spaces in-between.

![04](https://github.com/user-attachments/assets/c36c6296-db7e-4762-9051-49665e7a09c1)

## Credit

[Joell560](https://next.nexusmods.com/profile/Joell560?gameId=6945) for figuring out the shader replacement method and being kind enough to share his findings.

