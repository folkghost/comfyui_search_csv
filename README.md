Just a simple custom node created to do simple job.
I started to use comfyui since this March, after serveral month I kinda found my way of generating "random" image using different character loras. But there is always a problem to used the "correct" trigger words.
There are several nodes which can read trigger word from civitai or local file, but still, the tigger words cannot be modified as I need. So I started to create my own little table of certain loras with my tested trigger words.
There are also some case I would like to know which character was in the image generated, so with an additional column of character's name and the original franchise. So I can use the return value for naming the image or make generated padding titles.

To used the custom node, just download the .py file and put it into custom node folder of comfyui and restart your session. 
The node can be found under "util" category of nodes.
Users need to define the csv list with seperater of ";", and keywords to look for, also the desired output value column.

csv example:

character_loraA.safetensors;loraA_triggerword1, loraA_triggerword2,...,loraA_triggerwordn;Character nameA - Franchise nameA
character_loraB.safetensors;loraB_triggerword1, loraB_triggerword2,...,loraB_triggerwordn;Character nameB - Franchise nameB
...
