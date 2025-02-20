import multiprocessing

def square(n):
    print(f"Processing {n} squared: {n * n}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=square, args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes completed!")
