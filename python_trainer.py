import subprocess
import os
import time
import json
import numpy as np
from pathlib import Path

class CPPTransformerTrainer:
    def __init__(self, exe_path="FashionMNISTTransformer.exe"):
        """
        Wrapper de Python para tu Transformer en C++
        """
        self.exe_path = exe_path
        self.base_dir = Path(__file__).parent
        
        # RUTAS CORREGIDAS PARA TUS ARCHIVOS
        self.data_base_path = "C:/Users/andre/Downloads/fasshiob"
        
    def check_executable(self):
        """Verificar que el ejecutable existe"""
        if not os.path.exists(self.exe_path):
            raise FileNotFoundError(f"Ejecutable no encontrado: {self.exe_path}")
        print(f"✅ Ejecutable encontrado: {self.exe_path}")
    
    def check_data_files(self):
        """Verificar que los archivos de datos existen"""
        data_files = [
            "train-images-idx3-ubyte",
            "train-labels-idx1-ubyte", 
            "t10k-images-idx3-ubyte",
            "t10k-labels-idx1-ubyte"
        ]
        
        missing_files = []
        found_files = []
        
        for file in data_files:
            file_path = os.path.join(self.data_base_path, file)
            if not os.path.exists(file_path):
                missing_files.append(file_path)
            else:
                found_files.append(file_path)
                # Mostrar tamaño del archivo
                size_mb = os.path.getsize(file_path) / (1024 * 1024)
                print(f"✅ {file} ({size_mb:.1f} MB)")
        
        if missing_files:
            print(f"❌ Archivos faltantes:")
            for file in missing_files:
                print(f"   - {file}")
            return False
        
        print(f"✅ Todos los archivos de datos encontrados en {self.data_base_path}")
        return True
    
    def run_training(self, config=None):
        """
        Ejecutar el entrenamiento usando el C++ compilado
        """
        print("🚀 Iniciando entrenamiento con C++...")
        print("=" * 60)
        
        # Verificaciones
        self.check_executable()
        if not self.check_data_files():
            print("❌ No se pueden encontrar los archivos de datos")
            return False
        
        try:
            # Ejecutar el programa C++
            start_time = time.time()
            
            print(f"🔄 Ejecutando: {self.exe_path}")
            print("📊 Salida del programa:")
            print("-" * 50)
            
            # Ejecutar con output en tiempo real
            process = subprocess.Popen(
                [self.exe_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Leer output en tiempo real
            output_lines = []
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    line = output.strip()
                    print(line)
                    output_lines.append(line)
            
            # Obtener código de salida
            return_code = process.poll()
            end_time = time.time()
            
            print("-" * 50)
            
            if return_code == 0:
                print(f"✅ Entrenamiento completado exitosamente!")
                print(f"⏱️ Tiempo total: {end_time - start_time:.2f} segundos")
                
                # Extraer métricas del output
                self.extract_metrics(output_lines)
                return True
            else:
                stderr_output = process.stderr.read()
                print(f"❌ Error en el entrenamiento (código: {return_code}):")
                print(stderr_output)
                return False
                
        except Exception as e:
            print(f"❌ Error ejecutando el programa: {e}")
            return False
    
    def extract_metrics(self, output_lines):
        """Extraer métricas del output del programa"""
        print("\n📈 Métricas extraídas:")
        
        for line in output_lines:
            if "Test Accuracy:" in line:
                print(f"   🎯 {line}")
            elif "Test Loss:" in line:
                print(f"   📉 {line}")
            elif "Average Accuracy:" in line:
                print(f"   📊 {line}")
            elif "parameters:" in line.lower():
                print(f"   🔢 {line}")
    
    def run_multiple_configs(self):
        """
        Ejecutar múltiples configuraciones de entrenamiento
        """
        print("\n🔄 Modo de múltiples ejecuciones")
        print("Nota: El programa C++ usa configuración fija, pero podemos ejecutarlo varias veces")
        
        num_runs = 3
        results = []
        
        for i in range(1, num_runs + 1):
            print(f"\n🏃 Ejecución {i}/{num_runs}")
            print("=" * 40)
            
            success = self.run_training()
            results.append({
                "run": i,
                "success": success,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
            })
            
            if not success:
                print(f"❌ Falló la ejecución {i}")
                break
            
            if i < num_runs:
                print(f"⏳ Pausa de 3 segundos antes de la siguiente ejecución...")
                time.sleep(3)
        
        return results

def compile_cpp():
    """
    Compilar el código C++ automáticamente
    """
    print("🔨 Compilando código C++...")
    
    # Verificar que los archivos fuente existen
    source_files = [
        "main.cpp",
        "src/matrix.cpp", 
        "src/mnist_loader.cpp", 
        "src/transformer.cpp"
    ]
    
    missing_sources = []
    for file in source_files:
        if not os.path.exists(file):
            missing_sources.append(file)
    
    if missing_sources:
        print(f"❌ Archivos fuente faltantes: {missing_sources}")
        return False
    
    compile_cmd = [
        "g++", 
        "-std=c++14",  # Cambiado a C++14 para compatibilidad
        "-O2", 
        "-I./include",
        "-o", "FashionMNISTTransformer.exe"
    ] + source_files
    
    try:
        print(f"📝 Comando: {' '.join(compile_cmd)}")
        result = subprocess.run(
            compile_cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Compilación exitosa!")
            # Verificar que el ejecutable se creó
            if os.path.exists("FashionMNISTTransformer.exe"):
                size_kb = os.path.getsize("FashionMNISTTransformer.exe") / 1024
                print(f"📦 Ejecutable creado: FashionMNISTTransformer.exe ({size_kb:.1f} KB)")
            return True
        else:
            print(f"❌ Error de compilación:")
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error ejecutando compilador: {e}")
        return False

def run_benchmark():
    """
    Ejecutar benchmark de rendimiento
    """
    print("📊 Ejecutando benchmark de rendimiento...")
    
    trainer = CPPTransformerTrainer()
    
    # Múltiples ejecuciones para benchmark
    times = []
    accuracies = []
    
    for i in range(3):
        print(f"\n🏃 Ejecución de benchmark {i+1}/3")
        start = time.time()
        success = trainer.run_training()
        end = time.time()
        
        if success:
            times.append(end - start)
        else:
            print(f"❌ Falló la ejecución {i+1}")
            break
    
    if times:
        avg_time = np.mean(times) if len(times) > 1 else times[0]
        std_time = np.std(times) if len(times) > 1 else 0
        
        print(f"\n📈 Estadísticas de rendimiento:")
        print(f"   🕐 Tiempo promedio: {avg_time:.2f}s")
        if len(times) > 1:
            print(f"   📏 Desviación estándar: {std_time:.2f}s")
            print(f"   ⚡ Tiempo mínimo: {min(times):.2f}s")
            print(f"   🐌 Tiempo máximo: {max(times):.2f}s")
        print(f"   🔢 Número de ejecuciones: {len(times)}")

def check_system_requirements():
    """Verificar requisitos del sistema"""
    print("🔍 Verificando requisitos del sistema...")
    
    # Verificar g++
    try:
        result = subprocess.run(["g++", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✅ g++ encontrado: {version_line}")
        else:
            print("❌ g++ no encontrado")
            return False
    except:
        print("❌ g++ no encontrado en PATH")
        return False
    
    # Verificar espacio en disco
    import shutil
    free_space_gb = shutil.disk_usage('.').free / (1024**3)
    print(f"💾 Espacio libre: {free_space_gb:.2f} GB")
    
    return True

def main():
    """
    Función principal
    """
    print("🤖 Fashion-MNIST Transformer Trainer (Python + C++)")
    print("=" * 60)
    
    # Verificar sistema
    if not check_system_requirements():
        print("❌ Algunos requisitos no están disponibles")
        return
    
    while True:
        print("\n📋 Opciones disponibles:")
        print("1. 🔨 Compilar código C++")
        print("2. 🚀 Ejecutar entrenamiento único")
        print("3. 🔄 Ejecutar múltiples ejecuciones")
        print("4. 📊 Ejecutar benchmark")
        print("5. 🔍 Verificar archivos")
        print("6. 🗂️ Mostrar rutas de archivos")
        print("7. ❌ Salir")
        
        try:
            choice = input("\n👉 Selecciona una opción (1-7): ").strip()
            
            if choice == "1":
                if compile_cpp():
                    print("✅ Listo para entrenar!")
                else:
                    print("❌ Revisa los errores de compilación")
            
            elif choice == "2":
                trainer = CPPTransformerTrainer()
                trainer.run_training()
            
            elif choice == "3":
                trainer = CPPTransformerTrainer()
                results = trainer.run_multiple_configs()
                
                print("\n📊 Resumen de resultados:")
                for result in results:
                    status = "✅" if result["success"] else "❌"
                    print(f"{status} Ejecución {result['run']} - {result['timestamp']}")
            
            elif choice == "4":
                run_benchmark()
            
            elif choice == "5":
                trainer = CPPTransformerTrainer()
                trainer.check_executable()
                trainer.check_data_files()
            
            elif choice == "6":
                trainer = CPPTransformerTrainer()
                print(f"\n📁 Rutas de archivos:")
                print(f"   📊 Datos: {trainer.data_base_path}")
                print(f"   💻 Ejecutable: {trainer.exe_path}")
                print(f"   📂 Directorio actual: {os.getcwd()}")
            
            elif choice == "7":
                print("👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción inválida. Intenta de nuevo.")
        
        except KeyboardInterrupt:
            print("\n\n👋 Interrumpido por el usuario. ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()