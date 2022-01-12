""" The flags (answers) for the challenges. """
flags = {
    'Obedient Cat': {
        'flag': 'picoCTF{s4n1ty_v3r1f13d_2aa22101}',
        'solution': 'open the file in editor'
    },
    'Mod 26': {
        'flag': 'picoCTF{s4n1ty_v3r1f13d_2aa22101}',
        'solution': 'check rot13.py'
    },
    'Python Wrangling': {
        'flag': 'picoCTF{4p0110_1n_7h3_h0us3_67c6cc96}',
        'solution': 'inside the current path, '
                    'run "python 003_ende.py -d 003_flag.txt.en 67c6cc9667c6cc9667c6cc9667c6cc96" in a terminal'
    },
    'Wave a flag': {
        'flag': 'picoCTF{b1scu1ts_4nd_gr4vy_30e77291}',
        'solution': 'run "warm -h" in a linux terminal '
                    'after enabling execution of the file with the command "chmod +x warm"'
    },
    'information': {
        'flag': 'picoCTF{the_m3tadata_1s_modified}',
        'solution': 'since cat is also a command on linux, '
                    'tried converting the file to .txt and then using said command in the linux terminal.'
                    'I also used "| less" to show the contents page by page since I noticed that the file was big.'
                    'The first page contained some xml data and two promising strings.'
                    'Both of them failed so I tried decoding them using the code from previous challenges'
                    'Decoding the second string gave me the correct picoCTF flag'
    },
    'Nice netcat...': {
        'flag': 'picoCTF{g00d_k1tty!_n1c3_k1tty!_9b3b7392}',
        'solution': 'ran netcat command ($ nc) that was given on linux, got a list of integers as a response.'
                    'checked the first numbers against a ASCII table and it looked promising.'
                    'decoded the list using the python code in the repo and got a correct flag.'
    }
}
