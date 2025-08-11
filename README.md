# HCS Internal Selection 2025

Collection of challenges for HCS Internal Selection 2025 competition

```
<name>/
├── release/
│   └── ...
├── source/
│   └── <name>/
│       └── ...
└── poc/
    └── ...
└── README.md
```

Explanation:

1. **\<name>** is the name of the challenge to be created.  
2. **release** is the folder for the attachments to be given to the participants.  
3. **source** is the folder used to store the original challenge source code, and if it’s a service, this folder will be deployed to the server.

> Why does the source folder need another \<name>?  
> To avoid conflicts in docker compose so they don’t sync with each other

1. **poc** is the folder that contains an explanation of how to solve each challenge (mandatory).  
2. **README.md** is used to provide a description of each challenge. Below is a README.md template that can be used.

```md
# <name>

## Author

(discord username)

## Difficulty

Medium/Hard

## Description

lorem ipsum dolor sit amet.

HCS{example_flag}
```

## TIA 🕵️