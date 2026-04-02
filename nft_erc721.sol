// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// ERC721 NFT合约
contract NFTCollection {
    string public name = "BlockchainNFT";
    string public symbol = "BNFT";
    uint256 public tokenCount;

    mapping(uint256 => address) public ownerOf;
    mapping(uint256 => string) public tokenURI;

    event Transfer(address indexed from, address indexed to, uint256 indexed tokenId);

    function mint(address to, string memory _tokenURI) external returns (uint256) {
        tokenCount++;
        uint256 tokenId = tokenCount;
        ownerOf[tokenId] = to;
        tokenURI[tokenId] = _tokenURI;
        emit Transfer(address(0), to, tokenId);
        return tokenId;
    }

    function transfer(address to, uint256 tokenId) external {
        require(ownerOf[tokenId] == msg.sender, "Not the owner");
        ownerOf[tokenId] = to;
        emit Transfer(msg.sender, to, tokenId);
    }
}
