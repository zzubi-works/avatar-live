# Camera effects

Open **Studio → Effects**. Click an effect's heading to expand its controls, then turn on the switch on the right to apply it.

![Post effects, ambient occlusion and post-processing cards](img/guide-effects.png)

| Effect group | Editions |
|---|---|
| Post-processing | Basic / Pro |
| Advanced post effects | Pro |
| Ambient occlusion | Pro |

**Bloom and depth of field** appear in more than one group. Start by enabling one effect from one group at a time and compare the result. The reset icon in a heading resets that group; **Reset** at the bottom restores all effects.

<nav class="effect-index" aria-label="Find an effect" markdown="1">

[Anti-aliasing](#anti-aliasing) · [Bloom](#bloom) · [Color grading](#color-grading) · [Vignette](#vignette) · [Film grain](#film-grain) · [Chromatic aberration](#chromatic-aberration) · [Depth of field](#depth-of-field) · [Motion blur](#motion-blur)

Pro: [Color and tone](#color-and-tone) · [Sharpening and dithering](#sharpening-and-dithering) · [Anamorphic flares](#anamorphic-flares) · [Lens dirt](#lens-dirt) · [Night vision](#night-vision) · [Blur](#blur) · [Pixelation](#pixelation) · [Ambient occlusion](#ambient-occlusion-pro)

</nav>

## Post-processing

Adjust common colors, highlights and camera lens effects.

### Anti-aliasing

![Anti-aliasing selection](img/guide-post-aa.png)

Smooths jagged edges on hair and clothing.

| Option | Visible result |
|---|---|
| Off | Disables edge smoothing. |
| FXAA | Lightweight smoothing, but may slightly soften fine patterns. |
| SMAA | Smooths outlines while retaining more detail. |
| TAA | Stabilizes the image over time; moving objects may leave ghosting. |

### Bloom

![Bloom intensity, threshold and diffusion](img/guide-post-bloom.png)

Makes light spread around bright hair, glowing materials and accessories.

| Control | When increased |
|---|---|
| Intensity | The glow becomes stronger. |
| Threshold | Only brighter areas bloom; lower values let ordinary surfaces glow too. |
| Soft knee | The transition around the brightness threshold becomes gentler. |
| Diffusion | Light spreads across a larger area. |
| Anamorphic ratio | Stretches the glow horizontally or vertically. |
| Color | Sets the glow color. |

### Color grading

![Exposure, contrast, saturation, temperature and tint](img/guide-post-color.png)

| Control | Effect |
|---|---|
| Exposure | Higher brightens the whole image; lower darkens it. |
| Contrast | Increases the difference between highlights and shadows. |
| Saturation | Increases color intensity; lowering it approaches black and white. |
| Temperature | Lower appears cooler; higher gives a warmer tone. |
| Tint | Balances between green and magenta casts. |

### Vignette

![Vignette strength, softness and shape](img/guide-post-vignette.png)

Darkens the edges of the image to draw attention to its center.

- **Intensity:** Higher makes the edges darker.
- **Smoothness:** Higher spreads the transition over a wider region.
- **Roundness:** Changes the shape of the vignette.
- **Color:** Sets the color blended into the edges.

### Film grain

![Film grain intensity and size](img/guide-post-grain.png)

Adds fine film-like particles to the image.

- **Intensity:** Makes the grains more visible.
- **Size:** Makes the grains larger.
- **Colored:** Uses colored instead of monochrome grain.

### Chromatic aberration

![Chromatic aberration controls](img/guide-post-chromatic.png)

Separates red, green and blue near edges to simulate a lens defect. Greater intensity increases the separation.

### Depth of field

![Auto focus, aperture and lens settings](img/guide-post-dof.png)

Keeps the face in focus while blurring objects in front of and behind it.

| Control | Effect |
|---|---|
| Auto face focus | Tracks a moving face when enabled. |
| Focus distance | Sets the sharp distance when automatic focus is off. |
| Aperture | A **lower f-number** gives stronger foreground/background blur. |
| Focal length | Longer lenses make out-of-focus areas blur more easily. |
| Blur quality | Produces smoother blur but increases PC/GPU load. |

If the f-number is too low or focus distance is wrong, **the face itself can become blurry**.

### Motion blur

![Shutter angle and motion-blur sample count](img/guide-post-motion.png)

Adds trails to fast movement.

- **Shutter angle:** Higher creates longer motion trails.
- **Sample count:** Higher produces smoother trails but increases PC/GPU load.

## Advanced post effects (Pro)

A separate camera-effects group powered by Beautify. It appears as **Post Effects** in the UI.

### Color and tone

![Color and tone settings in advanced post effects](img/guide-fx-color.png)

| Control | Effect |
|---|---|
| LUT | Chooses a preset color-look filter. |
| LUT intensity | Strengthens the filter's color treatment. |
| ACES tonemapping | Changes how highlights and shadows are represented. |
| Saturation | Increases the strength of colors. |
| Contrast | Changes the gap between bright and dark areas. |
| Brightness | Adjusts overall brightness. |
| Tint color / intensity | Blends in a chosen color. At intensity **0**, the color remains invisible. |

### Sharpening and dithering

![Sharpness and dithering controls](img/guide-fx-sharpen.png)

- **Sharpen:** Makes outlines crisper. **0** disables it; excessive sharpening can make edges look rough.
- **Dithering:** Adds small noise to reduce visible color bands in smooth gradients.

### Bloom

![Distance attenuation and quality in advanced bloom](img/guide-fx-bloom.png)

- **Intensity:** Strength of the glow.
- **Threshold:** Higher limits bloom to brighter pixels.
- **Tint / intensity:** Color and amount added to the glow.
- **Distance attenuation:** Reduces bloom on distant objects.
- **Near attenuation distance:** Defines how nearby bloom should fall off.
- **High quality:** Improves the glow at additional processing cost.

### Anamorphic flares

![Anamorphic flare strength, spread and orientation](img/guide-fx-flares.png)

Creates long shafts of light extending from bright areas.

- **Intensity:** Brightens the shafts.
- **Threshold:** Higher limits the effect to brighter areas.
- **Spread:** Extends the light streaks farther.
- **Vertical:** On produces vertical streaks; off produces horizontal ones.
- **Tint / intensity:** Sets their color and tint strength.

### Depth of field

![Advanced depth of field, focus and bokeh](img/guide-fx-dof.png)

- **Auto head focus:** Follows the avatar's head.
- **Focus distance:** Manually sets the sharp distance when auto focus is off.
- **Focus speed:** Higher focuses on moving targets faster.
- **Lens / aperture:** Control how much of the scene is blurred.
- **Bokeh:** Turns blurred highlights into circular light spots.
- **Bokeh threshold:** Higher limits spots to brighter highlights.
- **Bokeh intensity:** Controls the spots' brightness.

Enabling **Blur** below turns this depth-of-field effect off.

### Chromatic aberration

![Strength and smoothing for advanced chromatic aberration](img/guide-fx-chromatic.png)

- **Intensity:** Increases the color separation around outlines.
- **Smoothing:** Softens how that separation changes across the image.

This effect is disabled when the background is **transparent**.

### Lens dirt

![Lens dirt textures and strength](img/guide-fx-dirt.png)

Overlays smudges on bright areas to simulate a dirty lens.

- **Texture:** Choose a dirt pattern; **None** disables it.
- **Intensity:** Makes the pattern more visible.
- **Threshold:** Brightness needed for the dirt effect.

### Vignette

![Advanced vignette settings](img/guide-fx-vignette.png)

- **Color:** Edge color.
- **Edge fade:** Amount of darkness at the edges.
- **Blink:** Controls a closing-eye-like screen-cover effect.

### Night vision

![Night vision and tint settings](img/guide-fx-night.png)

Creates a night-camera appearance in a chosen color. Enable its switch, then choose the effect color.

### Blur

![Full-screen blur settings](img/guide-fx-blur.png)

Blurs the **entire** picture. Increasing strength makes everything softer. To keep the face sharp while blurring the background, use **Depth of Field** instead.

### Pixelation

![Pixelation and pixel size](img/guide-fx-pixelate.png)

Turns the picture into large square pixels. Higher **pixel size** creates a coarser mosaic.

## Ambient occlusion (Pro)

![Ambient occlusion radius, strength and quality](img/guide-fx-hbao.png)

HBAO adds contact shadows where surfaces are close, such as under the chin, in clothing folds or at the corners of a room.

| Control | When increased |
|---|---|
| Radius | Shadows extend over a larger region. |
| Maximum radius | The maximum area used to calculate shadows grows. |
| Intensity | Contact shadows become darker. |
| Color | Changes the color of the shadows. |
| Quality | Shadows become smoother at a greater PC/GPU cost. |

If the eyes or nose become excessively dark, lower **intensity** or **radius**.

## Compare before and after

These examples show the same avatar and framing with actual effect values changed.

<div class="effect-pair" markdown="1">

![Bloom off](img/guide-example-bloom-off.png)

![Bloom on](img/guide-example-bloom-on.png)

</div>

<div class="effect-pair" markdown="1">

![Depth of field off](img/guide-example-dof-off.png)

![Strong depth-of-field example](img/guide-example-dof-on.png)

</div>

<div class="effect-pair" markdown="1">

![Vignette off](img/guide-example-vignette-off.png)

![Vignette on](img/guide-example-vignette-on.png)

</div>

<div class="effect-pair" markdown="1">

![Default color grading](img/guide-example-color-off.png)

![Reduced saturation](img/guide-example-color-on.png)

</div>

<div class="effect-pair" markdown="1">

![Pixelation off](img/guide-example-pixel-off.png)

![Pixelation on](img/guide-example-pixel-on.png)

</div>
