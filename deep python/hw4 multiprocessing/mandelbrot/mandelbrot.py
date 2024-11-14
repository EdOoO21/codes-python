import matplotlib.pyplot as plt
import multiprocessing,time

class MandelbrotGenerator:
    def __init__(self, num_workers: int):
        self.num_workers = num_workers

    def generate(self, width: int, height: int, max_iter: int) -> list[list[float]]:
        # Implement the parallel version of the Mandelbrot set generation
        start_time = time.time()
        image = multiprocessing.Array('i', width * height,lock=False)

        block_height = height // self.num_workers
        filled = []

        for i in range(self.num_workers):
            x1 = i * block_height
            if i < (self.num_workers - 1):
                x2 = (i + 1) * block_height
            else:
                x2 = height
            if x1 != x2:
                filled.append((image, x1, x2,width,height,max_iter))


        processes = [multiprocessing.Process(target=self.calc, args = [i]) for i in filled]

        for p in processes:
            p.start()

        i = 1
        for p in processes:
            elapsed_time = time.time() - start_time
            print(f"collecting {i} после {elapsed_time:.2f} секунд")
            p.join()
            elapsed_time = time.time() - start_time
            print(f"ended {i} после {elapsed_time:.2f} секунд")
            i += 1

        elapsed_time = time.time() - start_time
        print(f"started compile ans  после {elapsed_time:.2f} секунд")

        ans = [[image[(x*width) + y] for y in range(width)] for x in range(height)]

        elapsed_time = time.time() - start_time
        print(f"finished compile ans после {elapsed_time:.2f} секунд")

        return ans

    def calc(self, args):
            image,x1, x2,width,height,max_iter = args
            for x in range(x1, x2):
                for y in range(width):
                    z, n, c = 0, 0, self._scale(y, x, width, height)
                    while (abs(z) <= 2) and (n < max_iter):
                        z = (z**2) + c
                        n += 1

                    if (n == max_iter):
                        image[(x*width) + y] = 0
                    else:
                        image[(x*width) + y] = n

            return image

    @staticmethod
    def _scale(x: int, y: int, width: int, height: int) -> complex:
        return complex(3.5 * x / width - 2.5, 2 * y / height - 1)


def visualize(data: list[list[float]], colormap: str = 'magma', save_path: str | None = None) -> None:
    plt.imshow(data, cmap=colormap)
    # plt.colorbar()
    plt.axis('off')
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0, transparent=True, format='png')
    else:
        plt.show()
