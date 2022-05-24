pragma solidity ^0.5.16;
// version of solidity used

contract Election {
    // Store candidate
    // Read candidate
    string public candidate;
    // Constructor
    constructor() public {
        candidate = "Candidate 1";
    }
}
