from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()


class Processor(models.Model):
    processor_name = models.CharField('Сімейство процесора:', max_length=128, blank=True)
    processor_price = models.IntegerField('Ціна процесора:', default=0)
    processor_image = models.ImageField('Фото процесора:', upload_to='static/media/processor_image', blank=True)
    processor_producer = models.CharField('Виробник процесора:', max_length=32, blank=True)
    processor_socket = models.CharField('Тип сокета:', max_length=32, blank=True)
    processor_number_of_cores = models.SmallIntegerField('Кількість ядер:')
    processor_integrated_graphics = models.CharField('Інтегрована графіка:', max_length=64, blank=True)
    processor_frequency = models.CharField('Внутрішня частота:', max_length=24, blank=True)
    processor_max_frequency = models.CharField('Максимальна частота:', max_length=24, blank=True)
    processor_number_of_thread = models.SmallIntegerField('Кількість потоків:')
    processor_number_of_memory_channels = models.SmallIntegerField('Кількість каналів пам\'яті:')
    processor_type_of_memory = models.CharField('Тип пам\'яті процесора:', max_length=24, blank=True)

    def __str__(self):
        return'{processor_name}'.format(processor_name=self.processor_name)


class VideoCard(models.Model):
    video_card_name = models.CharField('Сімейство відеокатри:', max_length=128, blank=True)
    video_card_graphics_chip = models.CharField('Сімейство відеокатри:', max_length=128,  blank=True)
    video_card_image = models.ImageField('Фото відеокарти', upload_to='static/media/video_card_image', blank=True)
    video_card_price = models.IntegerField('Ціна відеокатри:', default=0)
    video_card_producer = models.CharField('Виробник відеокатри:', max_length=32, blank=True)
    video_card_cooling_system = models.CharField('Система охолодження :', max_length=64, blank=True)
    video_card_type_of_memory = models.CharField('Тип пам\'яті відеокатри:', max_length=24, blank=True)
    video_card_amount_of_memory = models.CharField('Обсяг пам\'яті відеокатри:', max_length=24, blank=True)
    video_card_bit_memory_bus = models.CharField('Розрядність шини пам\'яті', max_length=24, blank=True)
    video_card_minimum_required_power = models.CharField('Мінімально необхідна потужність БЖ', max_length=24,
                                                         blank=True)
    video_card_interface = models.CharField('Інтерфейс', max_length=32, blank=True)
    video_card_maximum_supported_resolution= models.CharField('Максимально підтримувана роздільна здатність:',
                                                              max_length=24, blank=True)

    def __str__(self):
        return ' {video_card_name}'.format(video_card_name=self.video_card_name)


class Motherboard(models.Model):
    motherboard_name = models.CharField('Назва материнської плати:', max_length=128, blank=True)
    motherboard_price = models.IntegerField('Ціна материнської плати:', default=0)
    motherboard_image = models.ImageField('Фото материнської плати', upload_to='static/media/motherboard_image',
                                          blank=True)
    motherboard_producer = models.CharField('Виробник материнської плати:', max_length=32, blank=True)
    motherboard_type = models.CharField('Тип розєму:', max_length=64, blank=True)
    motherboard_chip_set = models.CharField('Чипсет (Північний міст):', max_length=24, blank=True)
    motherboard_memory_support = models.CharField('Підтримка пам\'яті:', max_length=24, blank=True)
    motherboard_form_factor = models.CharField('Форм фактор:', max_length=24, blank=True)
    motherboard_number_of_memory_slots = models.SmallIntegerField('Кількість слотів пам\'яті')
    motherboard_processors_support = models.CharField('Підтрика процесорів:', max_length=128, blank=True)
    motherboard_maximum_amount_of_RAM = models.CharField('Назва материнської плати:', max_length=128, blank=True)

    def __str__(self):
        return '{motherboard_name}'.format(motherboard_name=self.motherboard_name)


class RAM(models.Model):
    RAM_name = models.CharField('Назва оперативної пам\'яті:', max_length=128, blank=True)
    RAM_price = models.IntegerField('Ціна оперативної пам\'яті:', default=0)
    RAM_image = models.ImageField("Фото оперативної пам\'яті", upload_to='static/media/RAM_image', blank=True)
    RAM_amount_of_memory = models.CharField('Обсяг пам\'яті:', max_length=24, blank=True)
    RAM_type_of_memory = models.CharField('Тип пам\'яті:', max_length=24, blank=True)
    RAM_supply_voltage = models.CharField('Напруга живлення:', max_length=24, blank=True)
    RAM_memory_frequency = models.CharField('Частота пам\'яті:', max_length=24, blank=True)
    RAM_effective_bandwidth = models.CharField('Ефективна пропускна здатність:', max_length=24, blank=True)
    RAM_number_of_slats = models.SmallIntegerField('Кількість планок:', default=0)
    RAM_producer = models.CharField('Виробник оперативної памяті:', max_length=32, blank=True)

    def __str__(self):
        return '{RAM_name}'.format(RAM_name=self.RAM_name)


class SSD(models.Model):
    SSD_name = models.CharField('Назва SSD диска:', max_length=128, blank=True)
    SSD_price = models.IntegerField('Ціна SSD диска:', default=0)
    SSD_image = models.ImageField('Фото ssd накопичувача', upload_to='static/media/SSD_image', blank=True)
    SSD_amount_of_memory = models.CharField('Обсяг пам\'яті:', max_length=24, blank=True)
    SSD_reading_speed = models.CharField('Швидкість читання:', max_length=24, blank=True)
    SSD_recording_speed = models.CharField('Швидкість запису:', max_length=24, blank=True)
    SSD_energy_consumption = models.CharField('Енергоспоживання:', max_length=68, blank=True)
    SSD_interface = models.CharField('Інтерфейс:', max_length=24, blank=True)
    SSD_type_of_memory_elements = models.CharField('Тип елементів пам\'яті:', max_length=24, blank=True)
    SSD_producer = models.CharField('Виробник SSD диска:', max_length=32, blank=True)

    def __str__(self):
        return '{SSD_name} '.format(SSD_name=self.SSD_name)


class Product(models.Model):
    processor = models.ForeignKey(Processor, related_name='processor', on_delete=models.CASCADE)
    video_card = models.ForeignKey(VideoCard, related_name='videocard', on_delete=models.CASCADE)
    motherboard = models.ForeignKey(Motherboard, related_name='motherboard', on_delete=models.CASCADE)
    ram = models.ForeignKey(RAM, related_name='ram', on_delete=models.CASCADE)
    ssd = models.ForeignKey(SSD, related_name='ssd', on_delete=models.CASCADE)
    published = PublishedManager()
