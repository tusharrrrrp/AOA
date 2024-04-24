def fractional_knapsack(values, weights, capacity):
    items = sorted(zip(values, weights), key=lambda x: x[0] / x[1], reverse=True) #sorted function sort karega pura andar ka  and zip will combine the values and wt and reverse will do the desecnding order work
    total_value = 0

    for i, j in items:
        if capacity >= j:
            total_value += i
            capacity -= j
        else:
            total_value += i * (capacity / j)
            break

    return total_value


#Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50


    print("Maximum value achievable:")
    print(fractional_knapsack(values, weights, capacity))
