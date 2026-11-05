class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) != len(cost):
            return -1
        gas_sum, cost_sum = 0, 0
        for value in gas:
            gas_sum += value
        for value in cost:
            cost_sum += value
        if cost_sum > gas_sum:
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
            
        return start  