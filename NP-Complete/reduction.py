# graph displaying Hamiltonian cycle
Ham = {
    "A" : {"B" , "D" },
    "B" : { "A" , "C"},
    "C": {"B", "D" },
    "D": {"C", "A"}
}

noHam = {
    "A": {"B" },
    "B": {"A" , "C"},
    "C": {"B", "D" },
    "D": {"C"}
}


# coversion function