def confinterval(size: int, x_mean, sigma, gamma, accuracy:int=0):
    from scipy.stats import norm
    """Args:
        size (int): sample size
        x_mean (float): sample average
        sigma (float): true standard deviation
        gamma (float): reliability level
        accuracy(int): number of decimal places, default = 0
       
    Returns:
        cotage: Confidence interval
    """
    alpha = 1 - gamma
    z_crit = -norm.ppf(alpha/2)
    eps = z_crit * sigma/(size ** 0.5) #погрешность
    lower_bound = x_mean - eps # левая (нижняя) граница
    upper_bound = x_mean + eps # правая (верхняя) граница
    confidence_interval = (round(lower_bound, 2), round(upper_bound, 2))
    
    return confidence_interval