import os
import shutil
from PIL import Image

def copy_images_based_on_match(folder_a, folder_b, folder_c):
    """
    フォルダAにある画像ファイルについて、フォルダBに同名のファイルがあればフォルダCにコピー。
    ない場合はフォルダAの画像をフォルダCにコピーします。

    Args:
        folder_a (str): フォルダAのパス
        folder_b (str): フォルダBのパス
        folder_c (str): フォルダCのパス
    """
    # フォルダCが存在しない場合、作成
    if not os.path.exists(folder_c):
        os.makedirs(folder_c)

    for file_name in os.listdir(folder_a):
        # 対象ファイルの拡張子チェック
        if file_name.lower().endswith(('jpg', 'jpeg', 'png', 'gif')):
            path_a = os.path.join(folder_a, file_name)
            path_b = os.path.join(folder_b, file_name)
            path_c = os.path.join(folder_c, file_name)

            # フォルダBに同名のファイルがある場合
            if os.path.exists(path_b):
                shutil.copy2(path_b, path_c)  # フォルダBのファイルをフォルダCにコピー
                print(f"フォルダBからコピー: {file_name}")
            else:
                shutil.copy2(path_a, path_c)  # フォルダAのファイルをフォルダCにコピー
                print(f"フォルダAからコピー: {file_name}")

def compress_images(input_folder, output_folder, quality=85):
    """
    指定フォルダ内の画像を圧縮して出力フォルダに保存します。

    Args:
        input_folder (str): 入力画像があるフォルダのパス
        output_folder (str): 圧縮画像を保存するフォルダのパス
        quality (int): 圧縮品質（1～100、デフォルトは85）
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                try:
                    # 入力画像のパス
                    input_path = os.path.join(root, file)
                    # 出力画像のパス
                    output_path = os.path.join(output_folder, file)

                    with Image.open(input_path) as img:
                        # PNGの場合、RGBに変換（PillowはPNGの圧縮に制限があるため）
                        if img.format == "PNG":
                            img = img.convert("RGB")
                        # 圧縮して保存
                        img.save(output_path, "JPEG", quality=quality)
                        print(f"圧縮成功: {file}")
                except Exception as e:
                    print(f"エラー発生: {file}, {e}")

if __name__=="__main__":


	# フォルダパスを設定
	folder_a = "../../Downloads/71247474-6646-4d50-8c8d-62e4b225fb76_Export-93d719dc-30b0-4ef0-89a6-e36b150b80d4/"
	folder_b = "../../Downloads/BharatPhotos/NamasteIndia/"
	folder_c = "../../Downloads/photos_to_use"

	# # 実行
	# copy_images_based_on_match(folder_a, folder_b, folder_c)


	# # 入力フォルダと出力フォルダを指定
	quality = 75
	input_folder = folder_c
	output_folder = f"../../Downloads/photos_compressed_{quality}"
	# output_folder = "./contents/"

	# # 圧縮実行
	compress_images(input_folder, output_folder, quality=quality)
