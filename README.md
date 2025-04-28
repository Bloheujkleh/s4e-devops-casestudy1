# AI Python Code Generator

Bu proje, kullanıcıdan bir istek (prompt) alır ve yapay zekâ destekli Python sınıfı üretir.  
Üretilen sınıflar, 'Task' tabanlıdır ve `run` ile `calculate_score` metodlarını içerir.

## Kurulum Adımları

1. Depoyu klonlayın:
   git clone https://github.com/kendi-repon-linkin.git
   cd ile kendi reponuza ulaşın

2. Gereken Python kütüphanelerini yükleyin:
   pip install -r requirements.txt

3. .env Dosyasını oluşturun:
   Proje ana dizinine .env dosyası oluşturup aşağıdaki formatta API anahtarınızı ekleyin:
   OPENAI_API_KEY=your-openai-api-key-here
(İlgili API anahtarı tarafımdan ayrıca e-posta ile iletilmiştir.)

4. Uygulamayı başlatın:
   python app.py

5. Tarayıcınızda açin:
   http://localhost:5000


* Docker Üzerinden açmak için;

1. Docker ile çalıştırmak

- docker pull bulent1234/ai-code-generator:latest

2. Uygulamayı Docker container olarak başlatmak için

- docker run -p 5000:5000 bulent1234/ai-code-generator:latest




* Minikube üzerinden deploy etmek için:

1. Kubernetes ortamında deploy etmek için:

- kubectl apply -f deployment.yaml




** OpenAI API Key doğrudan koda eklenmemiştir. .env dosyası üzerinden okunur.

** Docker imajı: bulent1234/ai-code-generator:latest


** Kubernetes Deployment dosyası (deployment.yaml) mevcuttur.