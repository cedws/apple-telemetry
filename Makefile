BLACKLIST=blacklist
RELEASE_DIR=release

all: cleanup gen-ip-blacklist gen-hosts gen-cloaking-rules

cleanup:
	sort -u -o $(BLACKLIST) $(BLACKLIST)

gen-ip-blacklist:
	mkdir -p $(RELEASE_DIR)
	echo "Generating IP blacklist, please be patient."
	utils/resolve.py < $(BLACKLIST) > $(RELEASE_DIR)/ip-blacklist
	sort -u -o $(RELEASE_DIR)/ip-blacklist $(RELEASE_DIR)/ip-blacklist

gen-hosts:
	mkdir -p $(RELEASE_DIR)
	sed 's/^/0.0.0.0 /' $(BLACKLIST) > $(RELEASE_DIR)/hosts

gen-cloaking-rules:
	mkdir -p $(RELEASE_DIR)
	sed 's/$$/ 0.0.0.0/' $(BLACKLIST) > $(RELEASE_DIR)/cloaking-rules
