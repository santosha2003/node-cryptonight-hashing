{
    "targets": [
        {
            "target_name": "cryptonight-hashing",
            "sources": [
                '<!@(uname -a | grep "amd64" >/dev/null && echo "xmrig/crypto/asm/cn_main_loop.S" || echo)',
                "multihashing.cc",
                "xmrig/extra.cpp",
                "xmrig/Mem_unix.cpp",
                "xmrig/crypto/c_blake256.c",
                "xmrig/crypto/c_groestl.c",
                "xmrig/crypto/c_jh.c",
                "xmrig/crypto/c_skein.c",
                "xmrig/common/crypto/keccak.cpp"
            ],
            "include_dirs": [
                "xmrig",
                "xmrig/3rdparty",
                "/usr/local/include",
                "<!(node -e \"require('nan')\")"
            ],
            "link_settings": {
                "libraries": [
                    "-L/usr/local/lib",
                    "-lboost_system",
                    "-lboost_date_time",
                ]
            },
            "cflags_c": [
                "-std=gnu11 -fPIC -DNDEBUG -Ofast -funroll-loops -fvariable-expansion-in-unroller -fmerge-all-constants"
            ],
            "cflags_cc": [
                "-std=gnu++11 -fPIC -DNDEBUG -Ofast -s -funroll-loops -fvariable-expansion-in-unroller -fmerge-all-constants"
                "-std=gnu11 -fPIC -DNDEBUG -Ofast -funroll-loops -fvariable-expansion-in-unroller -fmerge-all-constants"
            ],
            "cflags_cc": [
                "-std=gnu++11 -fPIC -DNDEBUG -Ofast -s -funroll-loops -fvariable-expansion-in-unroller -fmerge-all-constants "
            ]
        }
    ]
}
