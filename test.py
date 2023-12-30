import os
from src.preprocess.prepare_free_input import prepare_featured_input

materials = "Pak Satya, seorang pria bijaksana dengan sorot mata yang penuh pengalaman, telah menjadi pilar komunitas selama bertahun-tahun. Kehadirannya di desa ini tidak hanya tercermin dalam dedikasinya sebagai kepala dusun, tetapi juga dalam setiap tindakan kebaikan yang dilakukan untuk masyarakat sekitar. Dengan senyum ramahnya, Pak Satya kerap menjadi penengah dalam memecahkan masalah dan merangkul berbagai lapisan masyarakat. Ia dikenal sebagai sosok yang mendengarkan dengan penuh perhatian dan memberikan nasihat yang bijaksana. Di balik rambut abu-abunya, tersimpan kisah-kisah pengalaman hidup yang menjadi sumber inspirasi bagi banyak orang. Pak Satya bukan hanya seorang pemimpin, tetapi juga figur yang memancarkan kehangatan dan kebijaksanaan, mewarnai kehidupan sehari-hari di desa dengan kebaikan dan ketulusan hati."
prepare_featured_input(materials, output_file_name="free_input.txt", manual_ne_postag=False, lower=False, seed=42)
print("prepared data")
os.system(
        f'onmt_translate -model models/final/gru_037_cased_step_32100.pt \
            -src free_input.txt \
            -output free_input_pred.txt -replace_unk \
            -beam_size 2 \
            -max_length 4 \
            -verbose'
)
