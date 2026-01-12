import tensorflow as tf
from models import ProcessedImage

def process_image(image):
    # Загрузка модели GAN (псевдокод, это зависит от вашей модели)
    gan_model = tf.keras.models.load_model('path_to_gan_model')
    processed_image = gan_model.predict(image)
    
    # Сохранение обработанного изображения в базе данных
    processed_image_entry = ProcessedImage(image_id=image.id, style='Van Gogh', processing_date='2026-01-01')
    return processed_image_entry

def process_image_many(image, styles):
    results = []
    for style in styles:
        processed_image = gan_model.predict(image, style)
        results.append(processed_image)
    return results
