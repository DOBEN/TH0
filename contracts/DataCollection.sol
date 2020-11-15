// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "./SafeMath.sol";

contract DataCollection {
    using SafeMath for uint256;

    struct DataCollected {
        uint256 product_id;
		uint256 user_id;
		string[] types;
		uint256 count;
		uint256[] timestamps;
    }

    mapping (bytes32 => DataCollected) public mapData;

    function addDataCollected(uint256 product_id,uint256 user_id,string calldata input,uint256 timestamp) external {
	bytes32 key=keccak256(abi.encodePacked(product_id, user_id));
	uint256 old_count=mapData[key].count;
	old_count=old_count.add(1);
	uint256[] storage old_timestamps=mapData[key].timestamps;
	old_timestamps.push(timestamp);
	string[] storage old_types=mapData[key].types;
	old_types.push(input);
	
	mapData[key]=DataCollected(product_id, user_id, old_types, old_count, old_timestamps);
    }

    function readDataCount(uint256 product_id,uint256 user_id) external view returns (uint256){
		bytes32 key=keccak256(abi.encodePacked(product_id, user_id));
	return (mapData[key].count);
    }

    function readDataTimestamp(uint256 product_id,uint256 user_id,uint256 count) external view returns (uint256){
    	bytes32 key=keccak256(abi.encodePacked(product_id, user_id));
	return (mapData[key].timestamps[count]);
    }

 	function readDataType(uint256 product_id,uint256 user_id,uint256 count) external view returns (string memory){
    	bytes32 key=keccak256(abi.encodePacked(product_id, user_id));
	return (mapData[key].types[count]);
    }
}
