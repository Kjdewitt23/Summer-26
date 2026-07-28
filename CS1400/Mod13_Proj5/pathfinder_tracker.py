import matplotlib.pyplot as plt
import random

directions = ["up", "down", "left", "right"]

# Simulates an astronaut walking based on their individual choice weights
def spacewalk(astronaut):
    pos = astronaut["positions"]
    for i in range(500):
        rand_direction = random.choices(directions, weights=astronaut["weights"], k=1)[0]
        if rand_direction == "up":
            pos.append((pos[i][0], pos[i][1] + 1))
        elif rand_direction == "down":
            pos.append((pos[i][0], pos[i][1] - 1))
        elif rand_direction == "left":
            pos.append((pos[i][0] - 1, pos[i][1]))
        else:
            pos.append((pos[i][0] + 1, pos[i][1]))
    
    return astronaut
            

def plot_pathfinder_walk(astronaut):
    """
    Plots a single astronaut's spacewalk path and saves it as
    <name>_spacewalk.png.

    Expected astronaut dict keys:
        'name'      -> string, e.g. "Lance"
        'positions' -> list of (x, y) tuples
        'color'     -> matplotlib color, e.g. 'b', 'r', 'g'
        'marker'    -> matplotlib marker, e.g. 'o', 's', '^'
    """
    # Unpack the list of positions into x and y sequences
    xs, ys = zip(*astronaut['positions'])

    plt.figure(figsize=(10, 10))

    # Plot the points and the connecting path
    plt.scatter(
        xs,
        ys,
        color=astronaut['color'],
        edgecolor='k',
        alpha=0.7,
        s=100,
        marker=astronaut['marker']
    )
    plt.plot(xs, ys, lw=1.5, ls='--', color=astronaut['color'])

    plt.grid(True)
    plt.title(f'Pathfinder Spacewalk for {astronaut["name"]}')
    plt.xlabel('East-West')
    plt.ylabel('North-South')

    # Save to the required filename format, e.g. Lance_spacewalk.png
    plt.savefig(f'{astronaut["name"]}_spacewalk.png', dpi=300)
    plt.close()

def main():
    lance = {
        'name': 'Lance',
        'positions': [(0, 0)],
        'color': 'Blue',
        'marker': 'o',
        'weights': [1, 1, 1, 1],
    }

    sophie = {
        'name': 'Sophie',
        'positions': [(0, 0)],
        'color': 'Red',
        'marker': 's',
        'weights': [3, 1, 1, 1],
    }

    finn = {
            'name': 'Finn',
            'positions': [(0, 0)],
            'color': 'Green',
            'marker': '^',
            'weights': [0, 0, 1, 1],
        }

    spacewalk(lance)
    plot_pathfinder_walk(lance)

    spacewalk(sophie)
    plot_pathfinder_walk(sophie)

    spacewalk(finn)
    plot_pathfinder_walk(finn)

if __name__ == '__main__':
    main()
