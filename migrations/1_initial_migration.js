const Migrations = artifacts.require("Migrations");
const DataCollection = artifacts.require("DataCollection");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
  deployer.deploy(DataCollection);
};
