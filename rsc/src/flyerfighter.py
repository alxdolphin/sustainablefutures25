# Re-attempting to load the PSD file and extract layer details
from psd_tools import PSDImage

# Load the PSD file again
psd_path = "/Users/adalton/Projects/Sustainable Futures 2025/rsc/img/SF25Flyer.psd"
psd = PSDImage.open(psd_path)

# Extract detailed information about the layers
layer_details = []

for layer in psd:
    layer_details.append({
        "Name": layer.name,
        "Bounds": layer.bbox,
        "Visible": layer.visible,
        "Kind": layer.kind
    })

# Convert to DataFrame and display
df_layers = pd.DataFrame(layer_details)
tools.display_dataframe_to_user(name="PSD Layer Details", dataframe=df_layers)
