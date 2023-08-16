def ganache_connecter(array_of_dict):
    from web3 import Web3
    import json

    # Connect to Ganache
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

    # Ensure connection is established
    assert w3.is_connected()

    # Contract Address and ABI (replace with your actual values)
    contract_address = "0xbf19f33d255F864485de1524eBBB7C2EFEeA7b80"
    truffile = json.load(
        open("/Users/yash/HelloWorldNFTProject/build/contracts/HelloWorldNFT.json")
    )
    abi = truffile["abi"]

    # Initialize contract
    contract = w3.eth.contract(address=contract_address, abi=abi)

    # Fetch token information
    def get_token_info(token_id):
        # Call the 'getNFTData' function from the contract
        token_data = contract.functions.getNFTData(token_id).call()

        return {
            "instituteName": token_data[0],
            "degreeAssigned": token_data[1],
            "major": token_data[2],
        }

    # Example: Get information of token with tokenId = 1
    token_id = 1
    info = get_token_info(token_id)
    print(info)
    return info


if __name__ == "__main__":
    ganache_connecter()
