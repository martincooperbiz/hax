const CONFIG = {
  IMAGES_URL: "https://" + process.env.REACT_APP_DOMAIN + "/images/",
  CONTACT_URL: "https://" + process.env.REACT_APP_DOMAIN + "/api/contact",
  TOKEN: process.env.REACT_APP_TOKEN // API token - stored in SSM parameter
}

export default CONFIG;
