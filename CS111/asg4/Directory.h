struct Directory{
    char name[24];
    uint64_t creationtime;
    uint64_t modificationtime;
    uint64_t accesstime;
    uint32_t length;
    uint32_t start;
    uint32_t flags;
    uint32_t whitenoise;
};