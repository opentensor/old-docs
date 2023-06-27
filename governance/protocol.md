
## [governance]


Bittensor's governance protocol transitions network management from centralization within the foundation to community-ownership over time. The first stage of this management decentralization creates a bicameral legislature, in which the [Triumvirate](governance/triumvirate) creates proposals for the [Senate](governance/senate) to approve or veto. Triumvirate members are Opentensor Foundation employees, while the Senate is formed from the top K delegate hotkeys.

### [proposals]

Proposals are encapsulations of other extrinsics, which will only be executed after meeting two conditions:

1. Has obtained 50% + 1 approvals from the Senate
2. Has been closed by a member of the Triumvirate

This guarantees that Senate has to come to a majority consensus in order for a proposal to be executed. When a proposal is executed, the calldata that was passed to it during it's creation is then included in the same block as the close extrinsic.