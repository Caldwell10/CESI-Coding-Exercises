from cvrp_instance import generate_instance
import matplotlib.pyplot as plt

def plot_instance(coords):
    plt.scatter(coords[1:, 0], coords[1:, 1], color="blue", label="Customers") # customers
    plt.scatter(coords[0,0], coords[0: 1], color="red", marker="s", s=100, label="Depot") # depot

    for i in range(1, len(coords)):
        plt.annotate(str[i], coords[i, 0], coords[i, 1])

    plt.xlabel("x")
    plt.ylabel("x")
    plt.title("CVRP instance")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    coords, depot, customers, demand, num_vehicles, cost = generate_instance(5, 15, 42)
    

    


