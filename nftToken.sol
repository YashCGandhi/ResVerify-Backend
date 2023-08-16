// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HelloWorldNFT is ERC721, Ownable {
    struct NFTData {
        string instituteName;
        string degreeAssigned;
        string major;
    }

    mapping(uint256 => NFTData) private nftData;

    constructor(string memory _name, string memory _symbol) ERC721(_name, _symbol) {
    }

    // Mint a new token with additional data
    function mintToken(
        address _to,
        uint256 _tokenId,
        string memory _instituteName,
        string memory _degreeAssigned,
        string memory _major
    ) external onlyOwner {
        _mint(_to, _tokenId);
        nftData[_tokenId] = NFTData({
            instituteName: _instituteName,
            degreeAssigned: _degreeAssigned,
            major: _major
        });
        emit TokenMinted(_to, _tokenId);
    }

    // Transfer ownership of a token
    function transferToken(address _to, uint256 _tokenId) external {
        require(ownerOf(_tokenId) == msg.sender, "Only token owner can transfer");
        transferFrom(msg.sender, _to, _tokenId);
        emit TokenTransferred(msg.sender, _to, _tokenId);
    }

    // Get NFT data by token ID
    function getNFTData(uint256 _tokenId) external view returns (NFTData memory) {
        return nftData[_tokenId];
    }

    event TokenMinted(address indexed to, uint256 indexed tokenId);
    event TokenTransferred(address indexed from, address indexed to, uint256 indexed tokenId);
}
