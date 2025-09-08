import requests
import os 
def main():
    try:
        image_url = input("enter the url of image to download: ")
        folder_name = input("enter the folder name to save image: ")
        os.makedirs(folder_name, exist_ok=True)

        image_name = input("enter the image name with extension: ")
        image_path = os.path.join(folder_name, image_name)

        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"image saved successfully at {image_path}")
        else:
            print("failed to download image, status code:", response.status_code)

    except requests.exceptions.MissingSchema:
        print("invalid url, please enter a valid url")

    except Exception as e:
        print("an error occurred:", e)
        again = input("do you want to try again (y/n): ").strip().lower()
        if again == 'y':
            print("great, lets try again")
            main()  # retry
        else:
            print("exiting...")

    except KeyboardInterrupt:
        print("\nprocess interrupted, exiting...")

if __name__ == "__main__":
    main()
 

