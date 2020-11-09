RGBTRIPLE ogImage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            ogImage[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (i == 0 && j == 0)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i+1][j].rgbtRed
                + ogImage[i][j+1].rgbtRed + ogImage[i+1][j+1].rgbtRed) / 4.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i+1][j].rgbtGreen
                + ogImage[i][j+1].rgbtGreen + ogImage[i+1][j+1].rgbtGreen) / 4.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i+1][j].rgbtBlue
                + ogImage[i][j+1].rgbtBlue + ogImage[i+1][j+1].rgbtBlue) / 4.0);
            }
            else if (i == 0 && j == width - 1)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i+1][j].rgbtRed
                + ogImage[i][j-1].rgbtRed + ogImage[i+1][j-1].rgbtRed) / 4.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i+1][j].rgbtGreen
                + ogImage[i][j-1].rgbtGreen + ogImage[i+1][j-1].rgbtGreen) / 4.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i+1][j].rgbtBlue
                + ogImage[i][j-1].rgbtBlue + ogImage[i+1][j-1].rgbtBlue) / 4.0);
            }
            else if (i == 0)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i][j-1].rgbtRed + ogImage[i][j+1].rgbtRed
                + ogImage[i+1][j].rgbtRed + ogImage[i+1][j-1].rgbtRed + ogImage[i+1][j+1].rgbtRed) / 6.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i][j-1].rgbtGreen + ogImage[i][j+1].rgbtGreen
                + ogImage[i+1][j].rgbtGreen + ogImage[i+1][j-1].rgbtGreen + ogImage[i+1][j+1].rgbtGreen) / 6.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i][j-1].rgbtBlue + ogImage[i][j+1].rgbtBlue
                + ogImage[i+1][j].rgbtBlue + ogImage[i+1][j-1].rgbtBlue + ogImage[i+1][j+1].rgbtBlue) / 6.0);
            }
            else if (i == height - 1 && j == 0)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i-1][j].rgbtRed
                + ogImage[i][j+1].rgbtRed + ogImage[i-1][j+1].rgbtRed) / 4.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i-1][j].rgbtGreen
                + ogImage[i][j+1].rgbtGreen + ogImage[i-1][j+1].rgbtGreen) / 4.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i-1][j].rgbtBlue
                + ogImage[i][j+1].rgbtBlue + ogImage[i-1][j+1].rgbtBlue) / 4.0);
            }
            else if (j == 0)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i-1][j].rgbtRed + ogImage[i+1][j].rgbtRed
                + ogImage[i][j+1].rgbtRed + ogImage[i-1][j+1].rgbtRed + ogImage[i+1][j+1].rgbtRed) / 6.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i-1][j].rgbtGreen + ogImage[i+1][j].rgbtGreen
                + ogImage[i][j+1].rgbtGreen + ogImage[i-1][j+1].rgbtGreen + ogImage[i+1][j+1].rgbtGreen) / 6.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i-1][j].rgbtBlue + ogImage[i+1][j].rgbtBlue
                + ogImage[i][j+1].rgbtBlue + ogImage[i-1][j+1].rgbtBlue + ogImage[i+1][j+1].rgbtBlue) / 6.0);
            }
            else if (i == height - 1 && j == width - 1)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i-1][j].rgbtRed
                + ogImage[i][j-1].rgbtRed + ogImage[i-1][j-1].rgbtRed) / 4.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i-1][j].rgbtGreen
                + ogImage[i][j-1].rgbtGreen + ogImage[i-1][j-1].rgbtGreen) / 4.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i-1][j].rgbtBlue
                + ogImage[i][j-1].rgbtBlue + ogImage[i-1][j-1].rgbtBlue) / 4.0);
            }
            else if (i == height - 1)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i][j-1].rgbtRed + ogImage[i][j+1].rgbtRed
                + ogImage[i-1][j].rgbtRed + ogImage[i-1][j-1].rgbtRed + ogImage[i-1][j+1].rgbtRed) / 6.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i][j-1].rgbtGreen + ogImage[i][j+1].rgbtGreen
                + ogImage[i-1][j].rgbtGreen + ogImage[i-1][j-1].rgbtGreen + ogImage[i-1][j+1].rgbtGreen) / 6.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i][j-1].rgbtBlue + ogImage[i][j+1].rgbtBlue
                + ogImage[i-1][j].rgbtBlue + ogImage[i-1][j-1].rgbtBlue + ogImage[i-1][j+1].rgbtBlue) / 6.0);
            }
            else if (j == width - 1)
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i-1][j].rgbtRed + ogImage[i+1][j].rgbtRed
                + ogImage[i][j-1].rgbtRed + ogImage[i-1][j-1].rgbtRed + ogImage[i+1][j-1].rgbtRed) / 6.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i-1][j].rgbtGreen + ogImage[i+1][j].rgbtGreen
                + ogImage[i][j-1].rgbtGreen + ogImage[i-1][j-1].rgbtGreen + ogImage[i+1][j-1].rgbtGreen) / 6.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i-1][j].rgbtBlue + ogImage[i+1][j].rgbtBlue
                + ogImage[i][j-1].rgbtBlue + ogImage[i-1][j-1].rgbtBlue + ogImage[i+1][j-1].rgbtBlue) / 6.0);
            }
            else
            {
                image[i][j].rgbtRed = round((ogImage[i][j].rgbtRed + ogImage[i][j-1].rgbtRed + ogImage[i][j+1].rgbtRed
                + ogImage[i-1][j].rgbtRed + ogImage[i-1][j-1].rgbtRed + ogImage[i-1][j+1].rgbtRed
                + ogImage[i+1][j].rgbtRed + ogImage[i+1][j-1].rgbtRed + ogImage[i+1][j+1].rgbtRed) / 9.0);

                image[i][j].rgbtGreen = round((ogImage[i][j].rgbtGreen + ogImage[i][j-1].rgbtGreen + ogImage[i][j+1].rgbtGreen
                + ogImage[i-1][j].rgbtGreen + ogImage[i-1][j-1].rgbtGreen + ogImage[i-1][j+1].rgbtGreen
                + ogImage[i+1][j].rgbtGreen + ogImage[i+1][j-1].rgbtGreen + ogImage[i+1][j+1].rgbtGreen) / 9.0);

                image[i][j].rgbtBlue = round((ogImage[i][j].rgbtBlue + ogImage[i][j-1].rgbtBlue + ogImage[i][j+1].rgbtBlue
                + ogImage[i-1][j].rgbtBlue + ogImage[i-1][j-1].rgbtBlue + ogImage[i-1][j+1].rgbtBlue
                + ogImage[i+1][j].rgbtBlue + ogImage[i+1][j-1].rgbtBlue + ogImage[i+1][j+1].rgbtBlue) / 9.0);
            }
        }
    }
s