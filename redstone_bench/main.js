const { SmartWeaveNodeFactory, LoggerFactory } = require("redstone-smartweave");
const Arweave = require("arweave");

const arweave = Arweave.init({
  host: "arweave.net",
  port: 443,
  protocol: "https",
});

const smartweave = SmartWeaveNodeFactory.memCached(
  arweave,
);

(async () => {
  await SmartWeaveNodeFactory.fileCached(arweave, "./cached").contract("t9T7DIOGxx4VWXoCEeYYarFYeERTpWIC1V3y-BPZgKE").readState(749180);
})();
