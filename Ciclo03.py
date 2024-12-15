import rasterio
import numpy as np

def calculate_pixel_data(image_path):  # Parâmetro correto
    # Abrir a imagem TIFF
    with rasterio.open(image_path) as src:
        # Ler os dados da imagem como um array
        data = src.read(1)  # Lê a primeira banda (assumindo uma única banda)
        
        # Resolução da imagem (tamanho de um pixel em metros)
        pixel_area = src.transform[0] * abs(src.transform[4])  # largura * altura do pixel
        
        # Contagem de pixels
        total_pixels = data.size
        zero_pixels = np.sum(data == 0)
        soja_pixels = np.sum(data == 39)
        pastagem_pixels = np.sum(data == 15)

        # Conversão de pixels para hectares (1 hectare = 10,000 m²)
        hectares_per_pixel = pixel_area / 10000.0

        soja_area = soja_pixels * hectares_per_pixel
        pastagem_area = pastagem_pixels * hectares_per_pixel

        # Resultados
        return {
            "total_pixels": total_pixels,
            "zero_pixels": zero_pixels,
            "soja_pixels": soja_pixels,
            "pastagem_pixels": pastagem_pixels,
            "soja_area_hectares": soja_area,
            "pastagem_area_hectares": pastagem_area,
        }

# Caminho da imagem TIFF
image_path = r"coloque o caminho da imagem aqui"  # Use 'r' para strings com caminhos no Windows

# Processar e exibir os resultados
resultados = calculate_pixel_data(image_path)
print("Resultados:")
print(f"Quantidade total de pixels: {resultados['total_pixels']}")
print(f"Quantidade de pixels sem dados (código 0): {resultados['zero_pixels']}")
print(f"Quantidade de pixels de plantio de soja (código 39): {resultados['soja_pixels']}")
print(f"Área de plantio de soja: {resultados['soja_area_hectares']:.2f} hectares")
print(f"Quantidade de pixels de pastagem (código 15): {resultados['pastagem_pixels']}")
print(f"Área de pastagem: {resultados['pastagem_area_hectares']:.2f} hectares")
