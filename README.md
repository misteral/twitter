# Twitter Data Visualization Project

This project is designed to visualize Twitter user growth over time using a dataset of user counts. It includes a Python script that processes the data, interpolates missing values, and generates a video visualization of the user growth.

## Installation

To set up this project, you need to have Python installed on your system. This project uses Poetry for dependency management.

1. Clone the repository:
   ```
   git clone https://github.com/your-username/twitter-visualization.git
   ```
2. Navigate to the project directory:
   ```
   cd twitter-visualization
   ```
3. Install dependencies using Poetry:
   ```
   poetry install
   ```

## Usage

To generate the Twitter user growth video, run the following command:

```
poetry run python twitter/visualisation.py
```

The script will read the data from a JSON file, interpolate the missing dates, and create a video file named `output.mp4` by default.

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Follow me on twitter at @al_bobrov for more stuff like this.
