var Web3 = require('web3');
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
const start = 59;
const end = 99;

getBlocks(start,end)

async function getBlocks(start, end) {
    console.log("number,difficulty,gasLimit,totalDifficulty")
    for (let i = start; i <= end; i++) {
    var result =  await web3.eth.getBlock(i);
    console.log(result.number + "," + result.difficulty+ "," + result.gasLimit +  "," + result.totalDifficulty)
}
}

