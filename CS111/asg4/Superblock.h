struct Superblock{
    uint32_t magicnum;
    uint32_t totalblocks;
    uint32_t fatblocks;
    uint32_t blocksize;
    uint32_t root;
};